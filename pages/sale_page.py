from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class Sale(BasePage):
    page_url = '/sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        actual_text = header_title.text_content().strip()
        assert actual_text == text

    def check_link_text_womens_sale_is_correct(self, link_text):
        text_on_page = self.find(loc.womens_deals_loc)
        actual_text = text_on_page.text_content().strip()
        assert actual_text == link_text

    def check_link_text_mens_sale_is_correct(self, link_text):
        text_on_page = self.find(loc.mens_deals_loc)
        actual_text = text_on_page.text_content().strip()
        assert actual_text == link_text

    def check_discount_20_is(self, text):
        discount_text = self.find(loc.discount_20_off)
        actual_text = discount_text.text_content().strip()
        assert actual_text == text
