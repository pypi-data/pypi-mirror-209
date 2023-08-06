Асинхронная обёртка над [протоколом](https://chromedevtools.github.io/devtools-protocol/) отладчика браузера Chromium.

### Установка
```shell
pip install aio-dt-protocol
```

Имеет одну зависимость:
https://github.com/aaugustin/websockets

И так как всё общение через протокол основано на формате JSON, по желанию можно установить ujson:
https://github.com/ultrajson/ultrajson

### Примеры:

```python
import asyncio
from aio_dt_protocol import BrowserEx as Browser
from aio_dt_protocol import find_instances
from aio_dt_protocol.Data import KeyEvents

DEBUG_PORT: int = 9222
BROWSER_NAME: str = "chrome"


async def main() -> None:
    # ? Если на указанном порту есть запущенный браузер, происходит подключение.
    if browser_instances := find_instances(DEBUG_PORT, BROWSER_NAME):
        browser = Browser(debug_port=DEBUG_PORT, browser_pid=browser_instances[DEBUG_PORT])
        msg = f"[- CONNECT TO EXIST BROWSER ON {DEBUG_PORT} PORT -]"

    # ? Иначе, запуск нового браузера.
    else:
        browser = Browser(
            debug_port=DEBUG_PORT, browser_exe=BROWSER_NAME
        )
        msg = f"[- LAUNCH NEW BROWSER ON {DEBUG_PORT} PORT -]"
    print(msg)

    # ? Будет печатать в консоль всё, что приходит по соединению со страницей.
    # ? Полезно при разработке.
    # async def action_printer(data: dict) -> None:
    #     print(data)
    # page = await browser.GetPage(callback=action_printer)
    page = await browser.GetPage()

    print("[- GO TO GOOGLE ... -]")
    await page.Navigate("https://www.google.com")

    input_node = await page.QuerySelector("input")
    await input_node.Click()
    await asyncio.sleep(1)
    await page.action.InsertText("github PieceOfGood")
    await asyncio.sleep(1)
    await page.action.SendKeyEvent(KeyEvents.enter)
    await asyncio.sleep(1)

    submit_button_selector = "div:not([jsname])>center>[type=submit]:not([jsaction])"

    submit_button = await page.QuerySelector(submit_button_selector)
    await submit_button.Click()

    # ? Или выполнить клик используя JS
    # click_code = f"""\
    # document.querySelector("{submit_button_selector}").click();
    # """
    # await page.InjectJS(click_code)

    print("[- WAIT FOR CLOSE PAGE ... -]")
    # ? Пока соединение существует, цикл выполняется.
    await page.WaitForClose()
    print("[- DONE -]")


if __name__ == '__main__':
    asyncio.run(main())
```

На страницу можно легко зарегистрировать слушателей, которые будут вызываться на стороне клиентского(Python) кода. Для этого необходимо выполнить в браузере JavaScript, передав в `console.info()` JSON-строку из JavaScript-объекта с двумя обязательными полями `func_name` - имя вызываемой python-функции и `args` - список аргументов, которые будут ей переданы. Например:

```python
    html = """
    <html lang="ru">
    <head>
        <meta charset="utf-8" />
        <title>Test application</title>
    </head>
    <body>
        <button id="knopka">Push me</button>
    </body>
    <script>
        const btn = document.querySelector('#knopka');
        btn.addEventListener('click', () => {
            console.info(JSON.stringify({
                 func_name: "test_func",
                 args: [1, "test"]
            }))
        });
    </script>
    </html>"""

    # ? number и text будут переданы из браузера, а bind_arg указан при регистрации
    async def test_func(number: int, text: str, bind_arg: dict) -> None:
        print(f"[- test_func -] Called with args:\n\tnumber: {number}\n\ttext: {text}\n\tbing_arg: {bind_arg}")

    await page.AddListener(
        test_func,                          # ! слушатель
        {"name": "test", "value": True}     # ! bind_arg
    )

    # ? Если ожидается внушительный функционал прикрутить к странице, то это можно
    # ? сделать за один раз.
    # await page.AddListeners(
    #     (test_func, [ {"name": "test", "value": True} ]),
    #     # (any_awaitable1, [1, 2, 3])
    #     # (any_awaitable2, [])
    # )

    await page.Navigate(html)
```
### Headless
Чтобы запустить браузер в `безголовом` режиме, нужно передать аргументу принимающему путь к папке профиля пустую строку.
```python
import asyncio
from aio_dt_protocol import BrowserEx as Browser
from aio_dt_protocol.utils import save_img_as, async_util_call


async def main() -> None:
    print("[- HEADLESS RUN -]")
    browser = Browser(profile_path="")
    print("[- WAITING PAGE -]")
    page = await browser.WaitFirstTab()
    print("[- GO TO GOOGLE -]")
    await page.Navigate("https://www.google.com")
    
    print("[- MAKE SCREENSHOT -]")
    await async_util_call(
        save_img_as, "google.png", await page.MakeScreenshot()
    )
    
    print("[- CLOSE BROWSER -]")
    await page.CloseBrowser()
    print("[- DONE -]")

if __name__ == '__main__':
    asyncio.run(main())

```