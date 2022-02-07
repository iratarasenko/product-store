from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from .base_page import BasePage


class ItemPageLocators:
    item_title = (By.CLASS_NAME, 'name')
    add_button = (By.CLASS_NAME, 'btn-success')


class ItemPage(BasePage):

    url = 'https://www.demoblaze.com/prod.html?idp_={page_number}'

    def open(self, page_number):
        url = self.url.format(page_number=page_number)
        self.driver.get(url)
