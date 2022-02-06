from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from .base_page import BasePage


class ItemPageLocators:
    item_title = (By.CLASS_NAME, 'name')
    add_button = (By.CLASS_NAME, 'btn btn-success btn-lg')


class ItemPage(BasePage):

    @staticmethod
    def get_url(page_number):
        url = f'https://www.demoblaze.com/prod.html?idp_={page_number}'
        return url
