from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from ..locators import LoginPageLocators, AuthorizationPageLocators, HeaderLocators
from ..config import Config


class TestUserLogout():
    def test_user_login_success(self, driver:WebDriver, wait, go_to_authorization_page):
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT).send_keys(Config.EMAIL_REGISTERED)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT).send_keys(Config.PASSWORD)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME))
        driver.find_element(*AuthorizationPageLocators.LOGOUT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
        assert len(driver.find_elements(*HeaderLocators.USER_AVATAR)) == 0
        assert len(driver.find_elements(*HeaderLocators.USER_NAME)) == 0
        