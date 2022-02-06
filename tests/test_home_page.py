import time

import pytest
from selenium import webdriver
from pages.home_page import HomePage, HomePageLocators
from pages.item_page import ItemPage, ItemPageLocators


# Idea search for some before hook that will run automatically before each test

"""Test suite to verify category selection functionality at Home page"""
# Verify Home page name
@pytest.mark.home_page
def test_open_home_page(chrome_browser: webdriver.Chrome):
    home_page = HomePage(driver=chrome_browser)
    home_page.open()
    page_name = home_page.find(HomePageLocators.page_name)
    assert page_name.text == 'PRODUCT STORE'

# Verify number of displayed items after clicking on Monitors section
@pytest.mark.home_page
def test_open_monitors_category(chrome_browser: webdriver.Chrome):
    home_page = HomePage(driver=chrome_browser)
    home_page.open()
    home_page.click(HomePageLocators.get_category_name('Monitors'))
    time.sleep(1)
    displayed_monitors = home_page.find_many(HomePageLocators.items_in_section)
    assert len(displayed_monitors) == 2

# Verify that item with specified name is diaplayed on Monitors page
@pytest.mark.run
@pytest.mark.home_page
def test_open_item_from_monitors_category(chrome_browser: webdriver.Chrome):
    home_page = HomePage(driver=chrome_browser)
    home_page.open()
    home_page.click(HomePageLocators.get_category_name('Monitors'))
    time.sleep(1)
    home_page.click(HomePageLocators.get_item_in_section())
    apple_monitor_page = ItemPage(driver=chrome_browser)
    assert apple_monitor_page.find(ItemPageLocators.item_title).text == 'Apple monitor 24'
