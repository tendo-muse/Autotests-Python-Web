import allure
from selenium.common import TimeoutException

from pages.authorization.entryPage import EntryPage
from pages.mainPage import MainPage
from pages.authorization.jobSearchPage import JobSearchPage

# Вспомогательный класс шагов для автотестов
class AuthorizationSteps:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открыть главную страницу HH.ru")
    def open_main_page(self):
        self.browser.get("https://hh.ru/")
        return self

    @allure.step("Нажать кнопку входа")
    def click_login_button(self):
        MainPage(self.browser).login_button_click()
        return self

    @allure.step("Открыть страницу поиска работы")
    def open_job_search_page(self):
        MainPage(self.browser).login_button_click()
        EntryPage(self.browser).entry_button_click()
        return self

    @allure.step("Проверить отображение страницы поиска работы")
    def verify_job_search_page_displayed(self):
        job_search_page = JobSearchPage(self.browser)
        try:
            assert job_search_page.window_is_displayed(), "Не отображается страница поиска работы"
            assert 'Поиск работы' == job_search_page.title_text(), f"Ожидался заголовок 'Вход', получен '{job_search_page.title_text()}'"
        except TimeoutException:
            allure.attach(self.browser.get_screenshot_as_png())
        return self

    @allure.step("Проверить отображение страницы входа")
    def verify_entry_page_displayed(self):
        entry_page = EntryPage(self.browser)
        try:
            assert entry_page.window_is_displayed(), "Не отображается страница входа"
            assert 'Вход' == entry_page.title_text(), f"Ожидался заголовок 'Вход', получен '{entry_page.title_text()}'"
        except TimeoutException:
            allure.attach(self.browser.get_screenshot_as_png())
        return self
