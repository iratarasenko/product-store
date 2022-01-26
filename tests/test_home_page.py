from selenium import webdriver
from pages.home_page import HomePage

# Idea search for some before hook that will run automatically before each test

""" Test suite to verify category selection functionality at Home page """
def test_open_home_page(chrome_browser: webdriver.Chrome):
    home_page = HomePage(driver=chrome_browser)
    home_page.open_page()
    page_name = home_page.page_name.find()
    assert page_name.text == 'PRODUCT STORE'

def test_open_monitors_category(chrome_browser: webdriver.Chrome):
    home_page = HomePage(driver=chrome_browser)
    home_page.open_page()
    monitors_tab = home_page.get_category_name('Monitors')
    monitors_tab.click()
    print(home_page.get_monitors().find())
    
# # not a test
def select_most_expensive_monitor():
    pass



