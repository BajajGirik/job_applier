from playwright.async_api import async_playwright
from utils.env_helper import get_env
from utils.copy import copy_directory
from playwright_stealth import stealth_async


class WebBrowser:
    def __init__(self) -> None:
        # I accidentally corrupted my original profile while experimenting :')
        # So creating a copy of `user_data_dir` to keep the origin profile untouched
        self.__user_data_dir = copy_directory(get_env("USER_DATA_DIR"))


    async def setup(self) -> None:
        self.__playwright = await async_playwright().start()
        self.__context = await self.__playwright.chromium.launch_persistent_context(
            self.__user_data_dir,
            channel="chrome",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            headless=False,
            no_viewport=True,
            args= [
                "--start-maximized",
            ]
        )

        self.__page = await self.__context.new_page()
        await stealth_async(self.__page)



    async def destroy(self) -> None:
        await self.__context.close()
        await self.__playwright.stop()
