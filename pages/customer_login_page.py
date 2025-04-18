import allure

from pages.base_page import BasePage
from pages.locators import customer_login_locators as loc


class CustomerLogin(BasePage):
    page_url = '/customer/account/login/'

    @allure.step('Fill in the login form')
    def fill_in_login_form(self, login, password):
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        sign_in_button = self.get_by_role(*loc.sign_in_button_by_role)
        email_field.type(login)
        password_field.type(password)
        sign_in_button.click()

    def check_error_alert_text_is(self, required_text):
        with allure.step(f'Check error alert text is {required_text}'):
            actual_text = self.get_text_when_visible(loc.error_locator)
            assert actual_text == required_text, (
                f'Expected "{required_text}", Got "{actual_text}"'
            )
