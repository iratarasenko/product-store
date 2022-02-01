from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePageLocators:
    page_name = (By.ID, 'nava')
    items_in_section = (By.CLASS_NAME, 'card-title')

    @staticmethod
    def get_category_name(name):
        locator = (By.LINK_TEXT, name)
        return locator 


class HomePage(BasePage):
    
    url = 'https://www.demoblaze.com/index.html'
