from calendar import prcal
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .base_element import BaseElement


class HomePage(BasePage):
    
    url = 'https://www.demoblaze.com/index.html'

    @property
    def page_name(self):
       locator = (By.ID, 'nava')
       return BaseElement(
           driver = self.driver,
           by = locator[0],
           value = locator[1]
       )

    def get_category_name(self, name):
        locator = (By.LINK_TEXT, name)  
        return BaseElement(
            driver = self.driver,
            by = locator[0],
            value = locator[1]
        )

    def get_monitors(self):
        locator = (By.CLASS_NAME, 'card-title')
        return BaseElement(
            driver = self.driver,
            by = locator[0],
            value = locator[1]
        )