from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from ..locators import AuthorizationPageLocators, HeaderLocators
from ..config import Config


class TestUserLogin():
    def test_user_login_success(self, driver:WebDriver, wait, go_to_authorization_page):
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT).send_keys(Config.EMAIL_REGISTERED)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT).send_keys(Config.PASSWORD)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON).click()
        #ОЖИДАНИЕ: После регистрации должен быть редирект на главную страницу
        #БАГ: URL не меняется, хотя пользователь залогинен - тест упадет на следующем шаге. 
        #Info: Для проверки логина без смены URL закомментируй строчку assert driver.current_url == main_url 
        assert driver.current_url == Config.MAIN_URL 
        post_ad_button = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.POST_AD_BUTTON))
        assert post_ad_button.is_displayed()
        user_name = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME))
        assert user_name.text == Config.USER_NAME
        avatar = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_AVATAR))
        assert avatar.is_displayed()
