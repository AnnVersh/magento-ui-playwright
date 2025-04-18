import allure

from pages.base_page import BasePage
from pages.locators import ecofriendly_locators as loc


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_subsection_name(self, title):
        subsection_name = self.find(loc.eco_friendly_subsection)
        actual_text = subsection_name.text_content().strip()
        assert actual_text == title, (
            f'Expected: "{title}", Got: "{actual_text}"'
        )

    def check_menu_eco_option(self, eco_menu_option):
        menu_option = self.find(loc.eco_collection_menu_option)
        actual_option_text = menu_option.text_content().strip()
        assert actual_option_text == eco_menu_option, (
            f'Expected: "{eco_menu_option}", '
            f'Got: "{actual_option_text}"'
        )

    def check_reviews_subsection_opens(self, anchor):
        self.find(loc.product_reviews).click()
        with allure.step(f'Check that anchor "{anchor}" is present'):
            assert anchor in self.page.url, (
                f"URL does not contain '{anchor}'"
            )
