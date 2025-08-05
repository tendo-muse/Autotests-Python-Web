from pages.authorization.entryPage import EntryPage
from pages.authorization.jobSearchPage import JobSearchPage
from pages.mainPage import MainPage

def test_displayed_entry_page(browser):
    # Arrange
    browser.get("https://hh.ru/")

    # Act
    main_page = MainPage(browser)
    main_page.login_button_click()
    entry_page = EntryPage(browser)

    # Asserts
    assert True == entry_page.window_is_displayed
    assert 'Вход' == entry_page.title_text

def test_transition_job_search_page(browser):
    # Arrange
    browser.get("https://hh.ru/")

    # Act
    main_page = MainPage(browser)
    main_page.login_button_click()
    entry_page = EntryPage(browser)
    entry_page.entry_button_click()
    job_search_page = JobSearchPage(browser)

    # Asserts
    assert True == job_search_page.window_is_displayed
    assert 'Поиск работы' == job_search_page.title_text
