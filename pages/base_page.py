from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    url = None

    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def find(self, locator) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def find_many(self, locator):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return elements
    
    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.click()
        return None
        