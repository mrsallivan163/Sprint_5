from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from ..locators import LoginPageLocators, AuthorizationPageLocators, HeaderLocators, AdvertismentPageLocators


main_url = 'https://qa-desk.stand.praktikum-services.ru/'
email_registered = 'v.kilganov@mail.ru'
password = '1234567'
popup_text = 'Чтобы разместить объявление, авторизуйтесь'
name_ad = 'Объявление для теста'

class TestCreateAd():
    
    def test_create_ad_non_auth_user(self, driver:WebDriver, wait):
        driver.get(main_url)
        driver.find_element(*HeaderLocators.POST_AD_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(AuthorizationPageLocators.POPUP_AUTH))
        assert driver.find_element(*AuthorizationPageLocators.POPUP_AUTH).is_displayed()
        assert driver.find_element(*AuthorizationPageLocators.HEADER_POPUP_AUTH).text == popup_text

    def test_create_ad_auth_user(self, driver:WebDriver, wait, create_random_description, create_random_price, go_to_authorization_page):
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT).send_keys(email_registered)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(HeaderLocators.USER_NAME))
        driver.find_element(*HeaderLocators.POST_AD_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable(AdvertismentPageLocators.NAME))
        driver.find_element(*AdvertismentPageLocators.NAME).send_keys(name_ad)
        driver.find_element(*AdvertismentPageLocators.PRODUCT_DESCRIPTION).send_keys(create_random_description)
        driver.find_element(*AdvertismentPageLocators.PRICE).send_keys(create_random_price)
        wait.until(expected_conditions.element_to_be_clickable(AdvertismentPageLocators.DROP_CATEGORY)).click()
        driver.find_element(*AdvertismentPageLocators.CATEGORY).click()
        wait.until(expected_conditions.element_to_be_clickable(AdvertismentPageLocators.DROP_CITY)).click()
        driver.find_element(*AdvertismentPageLocators.CITY).click()
        driver.find_element(*AdvertismentPageLocators.RADIOBATTON).click()
        driver.find_element(*AdvertismentPageLocators.PUBLICATE_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(AdvertismentPageLocators.SEARCH_INPUT))
        driver.find_element(*HeaderLocators.USER_AVATAR).click()
        wait.until(expected_conditions.visibility_of_element_located(AdvertismentPageLocators.ADVERTISMENT))
        assert driver.find_element(*AdvertismentPageLocators.ADVERTISMENT).text == 'Объявление для теста'
