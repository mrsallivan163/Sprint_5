from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from ..locators import AuthorizationPageLocators, HeaderLocators


main_url = 'https://qa-desk.stand.praktikum-services.ru/'
email_registered = 'v.kilganov@mail.ru'
password = '1234567'

class TestUserLogin():
    def test_user_login_success(self, driver:WebDriver, wait, go_to_authorization_page):
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT).send_keys(email_registered)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON).click()
        #ОЖИДАНИЕ: После регистрации должен быть редирект на главную страницу
        #БАГ: URL не меняется, хотя пользователь залогинен - тест упадет на следующем шаге. 
        #Info: Для проверки логина без смены URL закомментируй строчку assert driver.current_url == main_url 
        assert driver.current_url == main_url 
        post_ad_button = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.POST_AD_BUTTON))
        assert post_ad_button.is_displayed()
        user_name = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME))
        assert user_name.text == 'User.'
        avatar = wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_AVATAR))
        assert avatar.is_displayed()
