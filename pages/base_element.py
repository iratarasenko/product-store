from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement():
    def __init__(self, driver, by, value) -> None:
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)

    def find(self) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator)
        )
        return element

    def click(self) -> None:
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()
        return None
