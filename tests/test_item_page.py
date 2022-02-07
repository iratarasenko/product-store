import pytest
from selenium import webdriver
from pages.item_page import ItemPage, ItemPageLocators
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.run
@pytest.mark.item_page
def test_add_to_cart(chrome_browser: webdriver.Chrome):
    """Verify add to card functionality"""
    item_page = ItemPage(driver=chrome_browser)
    item_page.open(page_number=10)
    item_page.click(ItemPageLocators.add_button)
    WebDriverWait(chrome_browser, 10).until(EC.alert_is_present())
    assert Alert(driver=chrome_browser).text == 'Product added'
