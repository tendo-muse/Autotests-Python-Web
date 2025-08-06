from selenium.webdriver.support.wait import WebDriverWait

from pages.authorization.baseAuthorizationPage import BaseAuthorizationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Модель страницы входа
class EntryPage(BaseAuthorizationPage):
    def __init__(self, browser):
        super().__init__(browser)

    def window_is_displayed(self):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@data-qa="applicant-login-card"]')))
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def entry_button_click(self):
        return self.browser.find_element(By.XPATH, '//button[@data-qa="submit-button"]').click()