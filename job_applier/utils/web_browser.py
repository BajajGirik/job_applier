from playwright.async_api import ElementHandle, async_playwright, Playwright, BrowserContext, Page
from utils.env_helper import get_env
from utils.copy import copy_directory
from playwright_stealth import stealth_async


class WebBrowser:
    def __init__(self, user_data_dir: str, playwright: Playwright, context: BrowserContext, page: Page) -> None:
        self.__user_data_dir = user_data_dir
        self.__playwright = playwright
        self.__context = context
        self.__page = page


    @classmethod
    async def create(cls):
        # I accidentally corrupted my original profile while experimenting :')
        # So creating a copy of `user_data_dir` to keep the origin profile untouched
        user_data_dir = copy_directory(get_env("USER_DATA_DIR"))

        playwright = await async_playwright().start()

        context = await playwright.chromium.launch_persistent_context(
            user_data_dir,
            channel="chrome",
            headless=False,
            no_viewport=True,
            args= [
                "--start-maximized",
            ]
        )

        page = await context.new_page()
        await stealth_async(page)


        return cls(user_data_dir, playwright, context, page)


    async def destroy(self) -> None:
        await self.__context.close()
        await self.__playwright.stop()


    async def open(self, url: str) -> None:
        await self.__page.goto(url)


    async def find_element(self, selector: str) -> ElementHandle | None:
        return await self.__page.query_selector(selector)
