from playwright.sync_api import BrowserContext

import pytest

from pages.create_new_customer_page import CreateNewCustomer
from pages.customer_login_page import CustomerLogin
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale


@pytest.fixture()
def sale_page(page):
    return Sale(page)


@pytest.fixture()
def customer_login_page(page):
    return CustomerLogin(page)


@pytest.fixture()
def create_new_customer_page(page):
    return CreateNewCustomer(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page
