from playwright.sync_api import Page
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        with allure.step(f'Open the page {self.page_url}'):
            if self.page_url:
                self.page.goto(f'{self.base_url}{self.page_url}')
            else:
                raise NotImplementedError(
                    "Page can't be opened for this page class"
                )

    @allure.step('Find element by locator')
    def find(self, locator):
        return self.page.locator(locator)

    @allure.step('Find by element role')
    def get_by_role(self, role, name):
        return self.page.get_by_role(role, name=name)

    def wait_for_url(self, expected_url):
        with allure.step(f'Wait for URL {expected_url}'):
            self.page.wait_for_url(expected_url, timeout=10000)  # 10 sec

    @allure.step('Return current URL')
    def current_url(self):
        return self.page.url

    def url_matches(self, expected_url):
        with allure.step(f'Check that URL is correct: {expected_url}'):
            self.wait_for_url(expected_url)
            assert self.current_url() == expected_url, (
                f"Expected: {expected_url}, "
                f"Got: {self.current_url()}"
            )

    def url_contains(self, expected_url_part):
        with allure.step(f'Check that URL contains: {expected_url_part}'):
            self.page.wait_for_url(
                f"**{expected_url_part}**",
                timeout=10000
            )
            assert expected_url_part in self.current_url(), (
                f'Expected URL part "{expected_url_part}" '
                f'not in "{self.current_url()}"'
            )

    def wait_until_visible(self, locator, timeout=10000):
        element = self.page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element

    def get_text_when_visible(self, locator):
        element = self.wait_until_visible(locator)
        # strip is used to return the text in a readable format
        return element.text_content().strip()

    def element_is_displayed(self, locator, timeout=10000):
        try:
            self.page.locator(locator).wait_for(
                state="visible",
                timeout=timeout
            )
            return True
        except Exception:
            return False
