from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()

