import allure

from steps.authorization.authorizationSteps import AuthorizationSteps

@allure.feature("Authorization")
@allure.story("Отображение страницы входа")
def test_displayed_entry_page(browser):
    # Arrange
    authorization_steps = AuthorizationSteps(browser)
    authorization_steps.open_main_page()

    # Act
    authorization_steps.click_login_button()

    # Asserts
    authorization_steps.verify_entry_page_displayed()

@allure.feature("Authorization")
@allure.story("Переход на страницу поиска работы")
def test_transition_job_search_page(browser):
    # Arrange
    authorization_steps = AuthorizationSteps(browser)
    authorization_steps.open_main_page()

    # Act
    authorization_steps.open_job_search_page()

    # Asserts
    authorization_steps.verify_job_search_page_displayed()
