from pages.base_page import BasePage
from pages.customer_account_page import CustomerAccountPage as CA
from pages.locators import create_new_customer_locators as loc

import allure

from utils.project_ec import (
    generate_random_email,
    generate_random_last_name,
    generate_random_first_name
)


class CreateNewCustomer(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill in the first name')
    def fill_in_first_name(self):
        first_name = generate_random_first_name()
        first_name_field = self.find(loc.first_name_field_loc)
        first_name_field.type(first_name)

    @allure.step('Fill in the last name')
    def fill_in_last_name(self):
        last_name = generate_random_last_name()
        last_name_field = self.find(loc.last_name_field_loc)
        last_name_field.type(last_name)

    @allure.step('Fill in the email')
    def fill_in_email(self):
        email = generate_random_email()
        email_field = self.find(loc.email_field_loc)
        email_field.type(email)

    @allure.step('Fill in the invalid email')
    def fill_in_invalid_email(self, email):
        email_field = self.find(loc.email_field_loc)
        email_field.type(email)

    @allure.step('Fill in the password')
    def fill_in_password(self, password):
        password_field = self.find(loc.password_filed_loc)
        password_field.type(password)

    @allure.step('Fill in the confirmation password')
    def fill_in_confirm_password(
            self, password
    ):
        confirm_password_filed = self.find(
            loc.confirm_password_filed_loc
        )
        confirm_password_filed.type(password)

    @allure.step('Click the "submit" button')
    def submit_form(self):
        self.find(loc.create_button_filed_loc).click()

    @allure.step('Fill in valid data and submit the form')
    def fill_and_submit_valid_form(self, password):
        self.fill_in_first_name()
        self.fill_in_last_name()
        self.fill_in_email()
        self.fill_in_password(password)
        self.fill_in_confirm_password(password)
        self.submit_form()
        self.url_matches(self.base_url + CA.page_url)

    @allure.step(
        'Check that error is displayed when non-matching passwd is entered'
    )
    def check_not_matching_passwords_error(
            self,
            password,
            incorrect_confirm_password
    ):
        self.fill_in_password(password)
        self.fill_in_confirm_password(incorrect_confirm_password)
        self.submit_form()
        assert self.element_is_displayed(loc.password_confirmation_error)

    @allure.step(
        'Check that error is displayed when invalid format email is entered'
    )
    def check_invalid_email_error(self, email):
        self.fill_in_invalid_email(email)
        self.submit_form()
        assert self.element_is_displayed(loc.email_address_error)
