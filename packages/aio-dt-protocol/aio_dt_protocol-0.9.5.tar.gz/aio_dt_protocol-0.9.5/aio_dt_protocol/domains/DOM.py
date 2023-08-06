import re
from abc import ABC, abstractmethod
from typing import Optional, Union, List
from ..DOMElement import Node
from ..domains.Runtime import RuntimeType
from ..exceptions import CouldNotFindNodeWithGivenID, RootIDNoLongerExists
from ..Data import DomainEvent

class DOM(ABC):
    """
    #   https://chromedevtools.github.io/devtools-protocol/tot/DOM
    """
    __slots__ = ()

    def __init__(self):
        self.dom_domain_enabled = False

    @property
    def connected(self) -> bool:
        return False

    @property
    def verbose(self) -> bool:
        return False

    @property
    def page_id(self) -> str:
        return ""

    async def DOMEnable(self) -> None:
        """
        Включает DOM-агент для данной страницы.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-enable
        :return:
        """
        await self.Call("DOM.enable")
        self.dom_domain_enabled = True

    async def DOMDisable(self) -> None:
        """
        Отключает DOM-агент для данной страницы.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-disable
        :return:
        """
        await self.Call("DOM.disable")
        self.dom_domain_enabled = False

    async def GetRoot(self, depth: Optional[int] = None, pierce: Optional[bool] = None) -> Node:
        """
        Возвращает корневой узел документа.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getDocument
        Корневой элемент ВСЕГДА имеет подобную структуру:
        'root': {
            'nodeId': 19,
            'backendNodeId': 2,
            'nodeType': 9,
            'nodeName': '#document',
            'localName': '',
            'nodeValue': '',
            'childNodeCount': 2,
            'children': [
                {
                    'nodeId': 20,
                    'parentId': 19,
                    'backendNodeId': 9,
                    'nodeType': 10,
                    'nodeName': 'html',
                    'localName': '',
                    'nodeValue': '',
                    'publicId': '',
                    'systemId': ''
                }, {
                    'nodeId': 21,
                    'parentId': 19,
                    'backendNodeId': 10,
                    'nodeType': 1,
                    'nodeName': 'HTML',
                    'localName': 'html',
                    'nodeValue': '',
                    'childNodeCount': 2,
                    'children': [
                        {
                            'nodeId': 22,
                            'parentId': 21,
                            'backendNodeId': 11,
                            'nodeType': 1,
                            'nodeName': 'HEAD',
                            'localName': 'head',
                            'nodeValue': '',
                            'childNodeCount': 4,
                            'attributes': [ ]
                        }, {
                            'nodeId': 23,
                            'parentId': 21,
                            'backendNodeId': 12,
                            'nodeType': 1,
                            'nodeName': 'BODY',
                            'localName': 'body',
                            'nodeValue': '',
                            'childNodeCount': 8,
                            'attributes': [ ]
                        }
                    ],
                    'attributes': [
                        'lang',
                        'ru'
                    ],
                    'frameId': 'AF11E1D7BC9DF951D77C6C07C02B98E7'
                }
            ],
            'documentURL': 'url ...',
            'baseURL': 'url ...',
            'xmlVersion': ''
        }
        :param depth:           Максимальная глубина, на которой должны быть извлечены
                                    дочерние элементы, по умолчанию равна 1. Используйте
                                    -1 для всего поддерева или укажите целое число больше 0.
        :param pierce:          Должны ли проходиться iframes и теневые корни при возврате
                                    поддерева (по умолчанию false).
        :return:            <Node>.
        """
        args = {}
        if depth is not None: args.update(depth=depth)
        if pierce is not None: args.update(pierce=pierce)
        node: dict = (await self.Call("DOM.getDocument", args))["root"]
        return Node(self, **node)

    async def QuerySelector(
            self, selector: str,
            ignore_root_id_exists: bool = False,
            in_frames: bool = False
    ) -> Union[Node, None]:
        """
        Выполняет DOM-запрос, возвращая объект найденного узла, или None.
            Эквивалент  === document.querySelector()
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-querySelector
        :param selector:                    Селектор.
        :param ignore_root_id_exists:       Игнорировать исключение при отсутствии родительского элемента.
                                                Полезно при запросах на загружающихся страницах.
        :param in_frames:                   Опрашивать документ вкючая shadow-root и iframe?
        :return:                <Node>
        """
        args = {} if not in_frames else dict(depth=-1, pierce=True)
        root_node_id = (await self.Call("DOM.getDocument", args))["root"]["nodeId"]
        try:
            node: dict = await self.Call("DOM.querySelector", {
                "nodeId": root_node_id, "selector": selector
            })
        except CouldNotFindNodeWithGivenID as e:
            if match := re.search(r"nodeId\': (\d+)", str(e)):
                if match.group(1) == str(root_node_id):
                    if ignore_root_id_exists:
                        return None
                    raise RootIDNoLongerExists
            raise
        return Node(self, **node) if node["nodeId"] > 0 else None


    async def QuerySelectorAll(
            self, selector: str,
            ignore_root_id_exists: bool = False,
            in_frames: bool = False
    ) -> List[Node]:
        """
        Выполняет DOM-запрос, возвращая список объектов найденных узлов, или пустой список.
            Эквивалент  === document.querySelectorAll()
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-querySelectorAll
        :param selector:                    Селектор.
        :param ignore_root_id_exists:       Игнорировать исключение при отсутствии родительского элемента.
                                                Полезно при запросах на загружающихся страницах.
        :param in_frames:                   Опрашивать документ вкючая shadow-root и iframe?
        :return:                [ <Node>, <Node>, ... ]
        """
        nodes = []
        args = {} if not in_frames else dict(depth=-1, pierce=True)
        root_node_id = (await self.Call("DOM.getDocument", args))["root"]["nodeId"]
        try:
            for node in (await self.Call("DOM.querySelectorAll", {
                "nodeId": root_node_id, "selector": selector
            }))["nodeIds"]:
                nodes.append(Node(self, node))
        except CouldNotFindNodeWithGivenID as e:
            if match := re.search(r"nodeId\': (\d+)", str(e)):
                if match.group(1) == str(root_node_id):
                    if ignore_root_id_exists:
                        return []
                    raise RootIDNoLongerExists
            raise
        return nodes

    async def PerformSearch(self, query: str, searchInShadowDOM: Optional[bool] = None) -> dict:
        """
        (EXPERIMENTAL)
        Ищет заданную строку в дереве DOM. Используйте 'GetSearchResults()' для доступа к результатам
            поиска или 'CancelSearch()'( !не найдено! ), чтобы завершить этот сеанс поиска. DOM-агент
            должен быть влючён.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-performSearch
        :param query:               Обычный текст, селектор, или поисковый запрос XPath.
        :param searchInShadowDOM:   (optional) True - поиск будет так же выполнен в shadow DOM.
        :return:                    {"searchId": str(searchId), "resultCount": int(resultCount)}
                                        searchId    - уникальный идентификатор сессии поиска.
                                        resultCount - кол-во результатов удовлетворяющих запрос.
        """
        args = {"query": query}
        if searchInShadowDOM is not None:
            args.update({"includeUserAgentShadowDOM": searchInShadowDOM})
        return await self.Call("DOM.performSearch", args)

    async def GetSearchResults(
            self, searchId: str,
            fromIndex: int = 0,
            toIndex:   int = 0
    ) -> List[Node]:
        """
        (EXPERIMENTAL)
        Возвращает список результатов поиска для поисковой сессии 'searchId', в интервале от 'fromIndex'
            до 'toIndex', полученной в результате вызова PerformSearch().
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getSearchResults
        :param searchId:        Уникальный идентификатор сессии поиска.
        :param fromIndex:       Начальный индекс результата поиска, который будет возвращен.
        :param toIndex:         Конечный индекс результата поиска, который будет возвращен.
        :return:                [ <Node>, <Node>, ... ]
        """
        nodes = []
        args = {"searchId": searchId, "fromIndex": fromIndex, "toIndex": toIndex}
        for node_id in (await self.Call("DOM.getSearchResults", args))["nodeIds"]:
            if self.verbose:
                print("[SearchResults] node_id =", node_id)
            nodes.append(Node(self, node_id, ""))
        return nodes

    async def Undo(self) -> None:
        """
        (EXPERIMENTAL)
        Отменяет последнее выполненное действие.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-undo
        :return:
        """
        await self.Call("DOM.undo")

    async def Redo(self) -> None:
        """
        (EXPERIMENTAL)
        Повторно выполняет последнее отмененное действие.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-redo
        :return:
        """
        await self.Call("DOM.redo")

    async def MarkUndoableState(self) -> None:
        """
        (EXPERIMENTAL)
        Отмечает последнее состояние, которое нельзя изменить.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-markUndoableState
        :return:
        """
        await self.Call("DOM.markUndoableState")

    async def DescribeNode(
            self, nodeId: Optional[int] = None,
            backendNodeId: Optional[int] = None,
            objectId: Optional[str] = None,
            depth: Optional[int] = None,
            pierce: Optional[bool] = None
    ) -> Node:
        """
        Описывает узел с учетом его идентификатора, не требует включения домена. Не начинает отслеживать какие-либо
            объекты, можно использовать для автоматизации.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-describeNode
        :return:
        """
        if not ((nodeId != None) | (backendNodeId != None) | (objectId != None)):
            raise ValueError("Один из nodeId, backendNodeId, или objectId — должен присутствовать!")
        args = {}
        if nodeId is not None: args.update(nodeId=nodeId)
        if backendNodeId is not None: args.update(backendNodeId=backendNodeId)
        if objectId is not None: args.update(objectId=objectId)
        if depth is not None: args.update(depth=depth)
        if pierce is not None: args.update(pierce=pierce)
        result = await self.Call("DOM.describeNode", args)
        return Node(self, **result["node"])

    async def ResolveNode(
            self, nodeId: Optional[int] = None,
            backendNodeId: Optional[int] = None,
            objectGroup: Optional[str] = None,
            executionContextId: Optional[str] = None
    ) -> RuntimeType.RemoteObject:
        """
        Создаёт JavaScript-объект для указанной ноды и возвращает его описание.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-resolveNode
        :return:
        """
        if not ((nodeId != None) | (backendNodeId != None)):
            raise ValueError("Один из nodeId, или backendNodeId — должен присутствовать!")
        args = {}
        if nodeId is not None: args.update(nodeId=nodeId)
        if backendNodeId is not None: args.update(backendNodeId=backendNodeId)
        if objectGroup is not None: args.update(objectGroup=objectGroup)
        if executionContextId is not None: args.update(executionContextId=executionContextId)
        result: dict = await self.Call("DOM.resolveNode", args)
        return RuntimeType.RemoteObject(**result.get("object"))

    async def RequestNode(self, objectId: str) -> Node:
        """
        Запрашивает, чтобы узел был отправлен вызывающей стороне с учетом ссылки на объект узла JavaScript.
            Все узлы, формирующие путь от узла к корню, также отправляются клиенту в виде серии
            setChildNodes-уведомлений.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-requestNode
        :return:
        """
        args = {"objectId": objectId}
        result: dict = await self.Call("DOM.requestNode", args)
        return Node(self, result.get("nodeId"))

    @abstractmethod
    async def Call(
            self, domain_and_method: str,
            params: Optional[dict] = None,
            wait_for_response: bool = True
    ) -> Union[dict, None]: raise NotImplementedError("async method Call() — is not implemented")


class DOMEvent(DomainEvent):
    attributeModified = "DOM.attributeModified"
    attributeRemoved = "DOM.attributeRemoved"
    characterDataModified = "DOM.characterDataModified"
    childNodeCountUpdated = "DOM.childNodeCountUpdated"
    childNodeInserted = "DOM.childNodeInserted"
    childNodeRemoved = "DOM.childNodeRemoved"
    documentUpdated = "DOM.documentUpdated"
    setChildNodes = "DOM.setChildNodes"
    distributedNodesUpdated = "DOM.distributedNodesUpdated"     # ! EXPERIMENTAL
    inlineStyleInvalidated = "DOM.inlineStyleInvalidated"       # ! EXPERIMENTAL
    pseudoElementAdded = "DOM.pseudoElementAdded"               # ! EXPERIMENTAL
    pseudoElementRemoved = "DOM.pseudoElementRemoved"           # ! EXPERIMENTAL
    shadowRootPopped = "DOM.shadowRootPopped"                   # ! EXPERIMENTAL
    shadowRootPushed = "DOM.shadowRootPushed"                   # ! EXPERIMENTAL
