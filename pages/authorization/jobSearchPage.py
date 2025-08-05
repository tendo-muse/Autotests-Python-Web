from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.authorization.baseAuthorizationPage import BaseAuthorizationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class JobSearchPage(BaseAuthorizationPage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def window_is_displayed(self):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@data-qa="applicant-login-card"]')))
            return element.is_displayed()
        except TimeoutException:
            return False
