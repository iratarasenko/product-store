import os

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@fixture
def chrome_browser():
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, os.pardir, 'chromedriver')
    service = Service(file_path)
    browser = webdriver.Chrome(service=service)
    yield browser
    browser.quit()