from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def login_button_click(self):
        return self.browser.find_element(By.XPATH, '//a[@data-qa="login"]').click()