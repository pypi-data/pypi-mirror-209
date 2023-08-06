import asyncio
from urllib.parse import quote
from abc import ABC, abstractmethod
from typing import Optional, Union, Callable, List, Literal
from ..Data import DomainEvent
from dataclasses import dataclass, field


class Page(ABC):
    """
    #   https://chromedevtools.github.io/devtools-protocol/tot/Page
    """
    __slots__ = ()

    def __init__(self):
        self.page_domain_enabled = False

    @property
    def connected(self) -> bool:
        return False

    @property
    def verbose(self) -> bool:
        return False

    @property
    def page_id(self) -> str:
        return ""

    @property
    def browser_name(self) -> str: return ""

    async def PageEnable(self) -> None:
        """
        Включает уведомления домена 'Page'.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-enable
        :return:
        """
        if not self.page_domain_enabled:
            await self.AddListenerForEvent("Page.frameStartedLoading", self._StateLoadWatcher, "started")
            await self.AddListenerForEvent("Page.frameNavigated", self._StateLoadWatcher, "navigated")
            await self.AddListenerForEvent("Page.frameStoppedLoading", self._StateLoadWatcher, "stopped")
            await self.Call("Page.enable")
            self.page_domain_enabled = True

    async def PageDisable(self) -> None:
        """
        Выключает уведомления домена 'Page'.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-disable
        :return:
        """
        if self.page_domain_enabled:
            self.RemoveListenerForEvent("Page.frameStartedLoading", self._StateLoadWatcher)
            self.RemoveListenerForEvent("Page.frameNavigated", self._StateLoadWatcher)
            self.RemoveListenerForEvent("Page.frameStoppedLoading", self._StateLoadWatcher)
            await self.Call("Page.disable")
            self.page_domain_enabled = False

    async def _StateLoadWatcher(self, params: dict, state: str) -> None:
        """
        Устанавливает состояние загрузки фрейма страницы, если включены уведомления
            домена Page.
        """
        frame_id = params["frameId"] if state != "navigated" else params["frame"]["id"]
        if frame_id == self.page_id:
            self.loading_state = state

    async def CreateIsolatedWorld(
            self, frameId: str, worldName: Optional[str] = None, grantUniversalAccess: Optional[bool] = None) -> int:
        """
        Создаёт изолированный мир для указанного фрейма.
        https://chromedevtools.github.io/devtools-protocol/1-3/Page/#method-createIsolatedWorld
        :param frameId:                 Идентификатор фрейма, в котором должен быть создан изолированный мир.
        :param worldName:               Необязательное имя, о котором сообщается в контексте выполнения.
        :param grantUniversalAccess:    Должен ли быть предоставлен универсальный доступ к изолированному миру.
                                            Это мощная опция, используйте ее с осторожностью.
        :return:            Runtime.ExecutionContextId
        """
        args = dict(frameId=frameId)
        if worldName is not None: args.update(worldName=worldName)
        if grantUniversalAccess is not None: args.update(grantUniversalAccess=grantUniversalAccess)
        result: dict = await self.Call("Page.createIsolatedWorld", args)
        return result.get("executionContextId")

    async def GetFrameTree(self) -> 'FrameTree':
        """
        Возвращает структуру присутствующих на странице фреймов. !!! Справедливо только в рамках одного домена.
        https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-getFrameTree
        """
        result = await self.Call("Page.getFrameTree")
        # print("Page.getFrameTree", result)
        return FrameTree(**result.get("frameTree"))

    # async def GetFrameFor

    async def HandleJavaScriptDialog(self, accept: bool, promptText: str = "") -> None:
        """
        Подтверждает или закрывает диалоговое окно, инициированное JavaScript (alert, confirm,
            prompt или для onbeforeunload).
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-handleJavaScriptDialog
        :param accept:          'True' — принять, 'False' — отклонить диалог.
        :param promptText:      (optional) Текст для ввода в диалоговом окне, прежде чем принять.
                                    Используется, только если это диалоговое окно с подсказкой.
        :return:
        """
        args = {"accept": accept}
        if promptText: args.update({"promptText": promptText})
        await self.Call("Page.handleJavaScriptDialog", args)

    async def Navigate(
            self,
            url:  Union[str, bytes] = "about:blank",
            wait_for_load:     bool = True,
            wait_for_complete: bool = False
    ) -> None:
        """
        Переходит на адрес указанного 'url'.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-navigate
        :param url:                 Адрес, по которому происходит навигация.
        :param wait_for_load:       (optional) Если 'True' - ожидает 'complete' у 'document.readyState'
                                        страницы, на которую осуществляется переход, а так же состояния остановки
                                        газрузки ресурсов, если активны уведомления домена Page.
        :param wait_for_complete:   (optional) Если 'True' - ожидает 'complete' у 'document.readyState'
                                        страницы, на которую осуществляется переход.
        :return:
        """
        b_name_len = len(self.browser_name)
        is_url = (
            "http" == url[:4] or
            "chrome" == url[:6] or
            self.browser_name == url[:b_name_len] or
            url == "about:blank"
        )
        if self.page_domain_enabled: self.loading_state = "do_navigate"
        _url_ = ("data:text/html," + quote(url)
             # передать разметку как data-url, если начало этой строки
             # не содержит признаков url-адреса или передать "как есть",
             if type(url) is str and not is_url else url
                 # раз это строка содержащая url, или переход на пустую страницу
                 if type(url) is str and is_url else
                     # иначе декодировать и установить её как Base64
                     "data:text/html;Base64," + url.decode()
             )

        await self.Call("Page.navigate", {"url": _url_})
        if wait_for_load:
            await self.WaitForLoad(ignore_loading_state=wait_for_complete)

    async def WaitForLoad(
        self,
        desired_state:         str = "complete",
        interval:            float = .1,
        ignore_loading_state: bool = False
    ) -> None:
        """
        Дожидается указанного состояния загрузки документа.
            Если включены уведомления домена Page — дожидается, пока основной фрейм
            страницы не перестанет загружаться.
        :param desired_state:           (optional) Желаемое состояние загрузки. По умолчанию == полное.
        :param interval:                (optional) Таймаут ожидания.
        :param ignore_loading_state:    (optional) Ожидать только состояния загрузки страницы?
        :return:        None
        """

        if self.page_domain_enabled and not ignore_loading_state:
            while self.loading_state != "stopped":
                await asyncio.sleep(.1)
        else: await asyncio.sleep(1)

        while (await self.Eval("document.readyState"))["value"] != desired_state:
            await asyncio.sleep(interval)

    async def WaitNavigate(
            self,
            url: Union[str, bytes] = "about:blank",
            wait_for_load: bool    = True,
            timeout: float         = 10.0
    ) -> bool:
        """
        Дожидается совершения перехода на адрес за указанный интервал времени возвращая True, или False,
            если дождаться не удалось.
        :param url:                 Адрес, по которому происходит навигация.
        :param wait_for_load:       (optional) Если 'True' - ожидает 'complete' у 'document.readyState'
                                        страницы, на которую осуществляется переход.
        :param timeout:             (optional) Кол-во секунд ожидания.
        :return:
        """
        try: await asyncio.wait_for(self.Navigate(url, wait_for_load), timeout)
        except asyncio.exceptions.TimeoutError: return False
        else: return True

    async def AddScriptOnLoad(self, src: str) -> str:
        """
        Запускает полученный 'src' скрипта в каждом фрейме и перед загрузкой скриптов самого фрейма.
            Так же, такой скрипт будет запускаться автоматически в течении всей жизни инстанса,
            включая перезагрузку страницы.
        Требует включения( PageEnable() ) уведомлений домена "Page".
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-addScriptToEvaluateOnNewDocument
        :param src:             Текст сценария.
        :return:                identifier -> Уникальный идентификатор скрипта.
        """
        if not self.page_domain_enabled: await self.PageEnable()
        return (await self.Call("Page.addScriptToEvaluateOnNewDocument", {"source": src}))["identifier"]

    async def RemoveScriptOnLoad(self, identifier: str) -> None:
        """
        Удаляет данный скрипт из списка запускаемых при загрузке фрейма.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-removeScriptToEvaluateOnNewDocument
        :param identifier:      Идентификатор сценария.
        :return:
        """
        await self.Call("Page.removeScriptToEvaluateOnNewDocument", {"identifier": identifier})

    async def SetDocumentContent(self, html: str, frameId: str = None) -> None:
        """
        Устанавливает полученную разметку как HTML-код документа.
            frameId — можно найти среди параметров события 'Runtime.executionContextCreated',
            а так же у корневого элемента документа root.children[1].frameId
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setDocumentContent
        :param html:            HTML-разметка.
        :param frameId:         Идентификатор фрейма, которому предназначается html.
        :return:
        """
        if frameId is None: frameId = self.page_id
        await self.Call("Page.setDocumentContent", {"frameId": frameId, "html": html})

    async def SetAdBlockingEnabled(self, enabled: bool) -> None:
        """
        (EXPERIMENTAL)
        Включите экспериментальный рекламный фильтр Chrome на всех сайтах.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setAdBlockingEnabled
        :param enabled:         Включить?
        :return:
        """
        if not self.page_domain_enabled: await self.PageEnable()
        await self.Call("Page.setAdBlockingEnabled", {"enabled": enabled})

    async def SetFontFamilies(self, fontFamilies: dict) -> None:
        """
        (EXPERIMENTAL)
        Установить общие семейства шрифтов.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setFontFamilies
        :param fontFamilies:    Семейства шрифтов:
                                    {
                                        "standard":   str(), -> (optional)
                                        "fixed":      str(), -> (optional)
                                        "serif":      str(), -> (optional)
                                        "sansSerif":  str(), -> (optional)
                                        "cursive":    str(), -> (optional)
                                        "fantasy":    str(), -> (optional)
                                        "pictograph": str(), -> (optional)
                                    }
        :return:
        """
        await self.Call("Page.setFontFamilies", {"fontFamilies": fontFamilies})

    async def SetFontSizes(self, fontSizes: dict) -> None:
        """
        (EXPERIMENTAL)
        Установите размеры шрифта по умолчанию.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setFontSizes
        :param fontSizes:       Определяет размеры шрифта для установки. Если размер шрифта не
                                    указан, он не будет изменен:
                                    {
                                        "standard": int(), -> (optional)
                                        "fixed":    int(), -> (optional)
                                    }
        :return:
        """
        await self.Call("Page.setFontSizes", {"fontSizes": fontSizes})

    async def CaptureScreenshot(
        self,
        format_: str = "",
        quality: int = -1,
        clip: Optional[dict] = None,
        fromSurface: bool = True
    ) -> str:
        """
        Сделать скриншот. Возвращает кодированное base64 представление скриншота.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-captureScreenshot
        :param format_:         string => Image compression format (defaults to png) (jpeg or png).
        :param quality:         integer => Compression quality from range [0..100] (jpeg only).
        :param clip:            {
                                    "x": "number => X offset in device independent pixels (dip).",
                                    "y": "number => Y offset in device independent pixels (dip).",
                                    "width": "number => Rectangle width in device independent pixels (dip).",
                                    "height": "number => Rectangle height in device independent pixels (dip).",
                                    "scale": "number => Page scale factor."
                                }
        :param fromSurface:     boolean => Capture the screenshot from the surface, rather than the view.
                                    Defaults to true.
        :return:                string => Base64-encoded image data.
        """
        args = {"fromSurface": fromSurface}
        if format_: args.update({"format": format_})
        if quality > -1 and format_ == "jpeg": args.update({"quality": quality})
        if clip: args.update({"clip": clip})
        return (await self.Call("Page.captureScreenshot", args))["data"]

    async def PrintToPDF(
        self,
        landscape:               Optional[bool] = None,
        displayHeaderFooter:     Optional[bool] = None,
        printBackground:         Optional[bool] = None,
        scale:                  Optional[float] = None,
        paperWidth:             Optional[float] = None,
        paperHeight:            Optional[float] = None,
        marginTop:              Optional[float] = None,
        marginBottom:           Optional[float] = None,
        marginLeft:             Optional[float] = None,
        marginRight:            Optional[float] = None,
        pageRanges:               Optional[str] = None,
        ignoreInvalidPageRanges: Optional[bool] = None,
        headerTemplate:           Optional[str] = None,
        footerTemplate:           Optional[str] = None,
        preferCSSPageSize:       Optional[bool] = None,
        transferMode:             Optional[str] = None
    ) -> dict:
        """
        Печатает страницу как PDF.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-printToPDF
        :param landscape:               (optional) Ориентация бумаги. По умолчанию false.
        :param displayHeaderFooter:     (optional) Отобразить header и footer. По умолчанию false.
        :param printBackground:         (optional) Печать фоновой графики. По умолчанию false.
        :param scale:                   (optional) Масштаб рендеринга веб-страницы. По умолчанию 1.
        :param paperWidth:              (optional) Ширина бумаги в дюймах. По умолчанию 8,5 дюймов.
        :param paperHeight:             (optional) Высота бумаги в дюймах. По умолчанию 11 дюймов.
        :param marginTop:               (optional) Верхний отступ в дюймах. По умолчанию 1 см (~ 0,4 дюйма).
        :param marginBottom:            (optional) Нижний отступ в дюймах. По умолчанию 1 см (~ 0,4 дюйма).
        :param marginLeft:              (optional) Левый отступ в дюймах. По умолчанию 1 см (~ 0,4 дюйма).
        :param marginRight:             (optional) Правый отступ в дюймах. По умолчанию 1 см (~ 0,4 дюйма).
        :param pageRanges:              (optional) Диапазон бумаги для печати, например, '1-5, 8, 11-13'. По
                                            умолчанию используется пустая строка, что означает печать всех страниц.
        :param ignoreInvalidPageRanges: (optional) Следует ли игнорировать недействительные, но успешно
                                            проанализированные диапазоны страниц, например '3-2'. По умолчанию false.
        :param headerTemplate:          (optional) HTML-шаблон для печатного заголовка. Должна быть допустимая
                                            разметка HTML со следующими классами, используемыми для вставки
                                            значений печати в них:
                                                * date:       formatted print date
                                                * title:      document title
                                                * url:        document location
                                                * pageNumber: current page number
                                                * totalPages: total pages in the document
                                                    Например, <span class=title></span> будет генерировать span,
                                                        содержащий заголовок.
        :param footerTemplate:          (optional) HTML-шаблон для печати 'footer'. Следует использовать тот же
                                            формат, что и headerTemplate.
        :param preferCSSPageSize:       (optional) Предпочитать или нет размер страницы, как определено CSS. По
                                            умолчанию установлено значение false, и в этом случае содержимое будет
                                            масштабироваться по размеру бумаги.
        :param transferMode:            (optional, EXPERIMENTAL) вернуть как поток. Допустимые значения:
                                            ReturnAsBase64, ReturnAsStream
        :return:                        {
                                            "data": str(Данные PDF, кодированные в Base64.),
                                                ->  Будет пустым если в 'transferMode' выбрано 'ReturnAsStream'.
                                            "stream": str(Это либо получается из другого метода, либо указывается как blob <uuid> это UUID Blob.)
                                                -> StreamHandle
                                        }
        """
        args = {}
        if landscape is not None:               args.update({"landscape": landscape})
        if displayHeaderFooter is not None:     args.update({"displayHeaderFooter": displayHeaderFooter})
        if printBackground is not None:         args.update({"printBackground": printBackground})
        if scale is not None:                   args.update({"scale": scale})
        if paperWidth is not None:              args.update({"paperWidth": paperWidth})
        if paperHeight is not None:             args.update({"paperHeight": paperHeight})
        if marginTop is not None:               args.update({"marginTop": marginTop})
        if marginBottom is not None:            args.update({"marginBottom": marginBottom})
        if marginLeft is not None:              args.update({"marginLeft": marginLeft})
        if marginRight is not None:             args.update({"marginRight": marginRight})
        if pageRanges is not None:              args.update({"pageRanges": pageRanges})
        if ignoreInvalidPageRanges is not None: args.update({"ignoreInvalidPageRanges": ignoreInvalidPageRanges})
        if headerTemplate is not None:          args.update({"headerTemplate": headerTemplate})
        if footerTemplate is not None:          args.update({"footerTemplate": footerTemplate})
        if preferCSSPageSize is not None:       args.update({"preferCSSPageSize": preferCSSPageSize})
        if transferMode is not None:            args.update({"transferMode": transferMode})

        return await self.Call("Page.printToPDF", args)

    async def Reload(
        self,
        ignoreCache: bool = False,
        scriptToEvaluateOnLoad: str = "",
        wait_for_load: bool = True
    ) -> None:
        """
        Перезагружает страницу инстанса, при необходимости игнорируя кеш.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-reload
        :param ignoreCache:             (optional) Игнорировать кеш?
        :param scriptToEvaluateOnLoad:  (optional) Если установлено, сценарий будет вставлен во все
                                            фреймы проверяемой страницы после перезагрузки. Аргумент
                                            будет игнорироваться при перезагрузке источника dataURL.
        :param wait_for_load:           (optional) По умолчанию — дожидается полного завершения
                                            загрузки страницы(document.readyState === "complete").
                                            Установите False, если это поведение не требуется.
        :return:
        """
        if self.page_domain_enabled: self.loading_state = "do_reload"
        args = {}
        if ignoreCache:            args.update({"ignoreCache": ignoreCache})
        if scriptToEvaluateOnLoad: args.update({"scriptToEvaluateOnLoad": scriptToEvaluateOnLoad})
        await self.Call("Page.reload", args)
        if wait_for_load:
            await self.WaitForLoad()

    async def GetNavigationHistory(self) -> dict:
        """
        Возвращает историю навигации для текущей страницы.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getNavigationHistory
        :return:            {
                                "currentIndex": int(), -> Индекс текущей записи истории навигации.
                                "entries": list({
                                    "id": int(),  -> Уникальный идентификатор записи истории навигации.
                                    "url": str(), -> URL записи истории навигации.
                                    "userTypedURL": str(), -> URL, который пользователь ввел в строке URL.
                                    "title": str(), -> Название записи истории навигации.
                                    "transitionType": str(
                                        link, typed, address_bar, auto_bookmark, auto_subframe,
                                        manual_subframe, generated, auto_toplevel, form_submit,
                                        reload, keyword, keyword_generated, other
                                    ) -> Тип перехода.
                                }, ... ) -> Список записей истории навигации.
                            }
        """
        return await self.Call("Page.getNavigationHistory")

    async def NavigateToHistoryEntry(self, entryId: int) -> None:
        """
        Навигация текущей страницы к выбранной записи в истории навгации.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-navigateToHistoryEntry
        :param entryId:             Уникальный идентификатор записи для перехода.
        :return:
        """
        if self.page_domain_enabled: self.loading_state = "do_navigate"
        await self.Call("Page.navigateToHistoryEntry", {"entryId": entryId})

    async def ResetNavigationHistory(self) -> None:
        """
        Сбрасывает историю навигации для текущей страницы.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-resetNavigationHistory
        :return:
        """
        await self.Call("Page.resetNavigationHistory")

    async def SetInterceptFileChooserDialog(self, enabled: bool) -> None:
        """
        Перехватывает запросы выбора файлов и передает управление клиентам протокола. Когда включен перехват
            файлов, диалоговое окно выбора файлов не отображается. Вместо этого генерируется событие
            протокола Page.fileChooserOpened.
        https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setInterceptFileChooserDialog
        :param enabled:             Включить перехват?
        :return:
        """
        await self.Call("Page.setInterceptFileChooserDialog", {"enabled": enabled})

    @abstractmethod
    async def AddListenerForEvent(
            self, event: Union[str, DomainEvent], listener: Callable, *args: any) -> None:
        raise NotImplementedError("async method AddListenerForEvent() — is not implemented")

    @abstractmethod
    def RemoveListenerForEvent(self, event: str, listener: Callable) -> None:
        raise NotImplementedError("method RemoveListenerForEvent() — is not implemented")

    @abstractmethod
    async def Eval(
            self, expression: str,
            objectGroup:            str = "console",
            includeCommandLineAPI: bool = True,
            silent:                bool = False,
            returnByValue:         bool = False,
            userGesture:           bool = True,
            awaitPromise:          bool = False
    ) -> dict:
        raise NotImplementedError("async method Eval() — is not implemented")

    @abstractmethod
    async def Call(
            self, domain_and_method: str,
            params: Optional[dict] = None,
            wait_for_response: bool = True
    ) -> Union[dict, None]: raise NotImplementedError("async method Call() — is not implemented")


class PageEvent(DomainEvent):
    domContentEventFired = "Page.domContentEventFired"
    fileChooserOpened = "Page.fileChooserOpened"
    frameAttached = "Page.frameAttached"
    frameDetached = "Page.frameDetached"
    frameNavigated = "Page.frameNavigated"
    interstitialHidden = "Page.interstitialHidden"
    interstitialShown = "Page.interstitialShown"
    javascriptDialogClosed = "Page.javascriptDialogClosed"
    javascriptDialogOpening = "Page.javascriptDialogOpening"
    lifecycleEvent = "Page.lifecycleEvent"
    loadEventFired = "Page.loadEventFired"
    windowOpen = "Page.windowOpen"
    frameClearedScheduledNavigation = "Page.frameClearedScheduledNavigation"    # DEPRECATED
    frameScheduledNavigation = "Page.frameScheduledNavigation"                  # DEPRECATED
    backForwardCacheNotUsed = "Page.backForwardCacheNotUsed"                    # ! EXPERIMENTAL
    compilationCacheProduced = "Page.compilationCacheProduced"                  # ! EXPERIMENTAL
    documentOpened = "Page.documentOpened"                                      # ! EXPERIMENTAL
    frameRequestedNavigation = "Page.frameRequestedNavigation"                  # ! EXPERIMENTAL
    frameResized = "Page.frameResized"                                          # ! EXPERIMENTAL
    frameStartedLoading = "Page.frameStartedLoading"                            # ! EXPERIMENTAL
    frameStoppedLoading = "Page.frameStoppedLoading"                            # ! EXPERIMENTAL
    navigatedWithinDocument = "Page.navigatedWithinDocument"                    # ! EXPERIMENTAL
    screencastFrame = "Page.screencastFrame"                                    # ! EXPERIMENTAL
    screencastVisibilityChanged = "Page.screencastVisibilityChanged"            # ! EXPERIMENTAL
    downloadProgress = "Page.downloadProgress"                                  # * EXPERIMENTAL DEPRECATED
    downloadWillBegin = "Page.downloadWillBegin"                                # * EXPERIMENTAL DEPRECATED


@dataclass
class AdFrameStatus:
    """ Указывает, был ли frame идентифицирован как реклама и почему. """
    adFrameType: Literal["none", "child", "root"]
    explanations: Optional[List[Literal["ParentIsAd", "CreatedByAdScript", "MatchedBlockingRule"]]] = None


@dataclass
class Frame:
    """ Информация о фрейме на странице """
    id: str
    loaderId: str                               # ? Network.LoaderId
    url: str
    domainAndRegistry: str
    securityOrigin: str
    mimeType: str
    secureContextType: Literal["Secure", "SecureLocalhost", "InsecureScheme", "InsecureAncestor"]
    crossOriginIsolatedContextType: Literal["Isolated", "NotIsolated", "NotIsolatedFeatureDisabled"]
    gatedAPIFeatures: List[Literal[
        "SharedArrayBuffers", "SharedArrayBuffersTransferAllowed", "PerformanceMeasureMemory", "PerformanceProfile"
    ]]
    adFrameStatus: Optional['AdFrameStatus']
    parentId: Optional[str] = None
    name: Optional[str] = None
    urlFragment: Optional[str] = None
    unreachableUrl: Optional[str] = None
    _adFrameStatus: Optional['AdFrameStatus'] = field(init=False, repr=False, default=None)

    @property
    def adFrameStatus(self) -> Union['AdFrameStatus', None]:
        return self._adFrameStatus

    @adFrameStatus.setter
    def adFrameStatus(self, data: dict) -> None:
        self._adFrameStatus = AdFrameStatus(**data) if not isinstance(data, property) else None


@dataclass
class FrameTree:
    """ Информация об иерархии фреймов """
    frame: 'Frame'
    childFrames: Optional[List['FrameTree']]
    _childFrames: Optional[List['FrameTree']] = field(init=False, repr=False, default=None)

    @property
    def frame(self) -> 'Frame':
        return self._frame

    @frame.setter
    def frame(self, data: dict) -> None:
        self._frame = Frame(**data)

    @property
    def childFrames(self) -> Union[List['FrameTree'], None]:
        return self._childFrames

    @childFrames.setter
    def childFrames(self, data: List[dict]) -> None:
        if not isinstance(data, property):
            self._childFrames = [FrameTree(**frame_data) for frame_data in data]
        else:
            self._childFrames = None

    def GetFrameByUrl(self, value: str) -> Union['Frame', None]:
        def search(tree: 'FrameTree', value: str) -> Union['Frame', None]:
            print("tree.frame.url", tree.frame.url)
            if value in tree.frame.url:
                return tree.frame
            else:
                if tree.childFrames:
                    for child in tree.childFrames:
                        if result := search(child, value):
                            return result
            return None
        return search(self, value)
