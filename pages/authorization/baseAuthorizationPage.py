from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseAuthorizationPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def title_text(self):
        element = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[@data-qa="title"]')))
        return element.text