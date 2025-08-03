from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from ..locators import RegistrationPageLocators, HeaderLocators


invalid_email = 'mail'
email_registered = 'v.kilganov@mail.ru'
password = '1234567'
main_url = 'https://qa-desk.stand.praktikum-services.ru/'

class TestUserRegistration:

    def test_user_registration_success(self, driver:WebDriver, wait, create_unique_email, go_to_registration_page):
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(create_unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
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

    def test_user_registration_with_email_not_by_mask(self, driver:WebDriver, wait, go_to_registration_page):
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
        error_message = wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_MESSAGE))
        assert error_message.text == 'Ошибка'
        assert driver.find_element(*RegistrationPageLocators.RED_FIELD_EMAIL)
        assert driver.find_element(*RegistrationPageLocators.RED_FIELD_PASSWORD)
        assert driver.find_element(*RegistrationPageLocators.RED_FIELD_REPEAT_PASSWORD)

    def test_user_registration_of_an_existing(self, driver:WebDriver, wait, go_to_registration_page):
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email_registered)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
        error_message = wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.EMAIL_ERROR_MESSAGE))
        assert error_message.text == 'Ошибка'
        assert driver.find_element(*RegistrationPageLocators.RED_FIELD_EMAIL)
        assert driver.find_element(*RegistrationPageLocators.RED_FIELD_PASSWORD)
        assert driver.find_element(*RegistrationPageLocators.RED_FIELD_REPEAT_PASSWORD)    
