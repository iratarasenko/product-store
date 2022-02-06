from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePageLocators:
    page_name = (By.ID, 'nava')
    items_in_section = (By.CLASS_NAME, 'card-title')

    @staticmethod
    def get_category_name(name):
        locator = (By.LINK_TEXT, name)
        return locator

    @staticmethod
    def get_item_in_section():
        locator = (By.XPATH, '//a[text()="Apple monitor 24"]')
        return locator


class HomePage(BasePage):

    url = 'https://www.demoblaze.com/index.html'

    def get_element_by_text(self, text):
        elements = self.find_many(HomePageLocators.items_in_section)
        for element in elements:
            if element.text == text:
                return element
