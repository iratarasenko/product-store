class BasePage():

    url = None

    def __init__(self, driver) -> None:
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)
    