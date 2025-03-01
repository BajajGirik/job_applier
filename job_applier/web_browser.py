from playwright.async_api import async_playwright
from utils.env_helper import get_env

class WebBrowser:
    def __init__(self) -> None:
        self.__user_data_dir = get_env("USER_DATA_DIR")


    async def setup(self) -> None:
        self.__playwright = await async_playwright().start()
        self.__context = await self.__playwright.chromium.launch_persistent_context(self.__user_data_dir, channel="chrome", headless=False)


    async def destroy(self) -> None:
        await self.__context.close()
        await self.__playwright.stop()
