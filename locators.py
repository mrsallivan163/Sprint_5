from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")

class RegistrationPageLocators():
    EMAIL_INPUT = (By.XPATH, ".//input[@placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@placeholder='Пароль']")
    REPEAT_PASSWORD_INPUT = (By.XPATH, ".//input[@placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Создать аккаунт')]")
    EMAIL_ERROR_MESSAGE = (By.XPATH, ".//input[@name='email']/following::span[@class='input_span__yWPqB' and text()='Ошибка']")
    RED_FIELD_EMAIL = (By.XPATH, ".//input[@name='email']/ancestor::div[contains(@class, 'input_inputError__fLUP9')]")
    RED_FIELD_PASSWORD = (By.XPATH, ".//input[@name='password']/ancestor::div[contains(@class, 'input_inputError__fLUP9')]")
    RED_FIELD_REPEAT_PASSWORD = (By.XPATH, ".//input[@name='submitPassword']/ancestor::div[contains(@class, 'input_inputError__fLUP9')]")

class HeaderLocators():
    USER_NAME = (By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/div[@class='flexRow']/div/h3[@class='profileText name']")
    USER_AVATAR = (By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/div[@class='flexRow']/button[@class='circleSmall']")
    POST_AD_BUTTON = (By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[text()='Разместить объявление']")

class AuthorizationPageLocators():
    EMAIL_INPUT = (By.XPATH, ".//input[@placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выйти')]")
    POPUP_AUTH = (By.CLASS_NAME, 'popUp_shell__LuyqR')
    HEADER_POPUP_AUTH = (By.XPATH, ".//form/div[@class='popUp_titleRow__M7tGg']")

class AdvertismentPageLocators():
    NAME = (By.XPATH, ".//input[@placeholder = 'Название']")
    PRODUCT_DESCRIPTION = (By.XPATH, ".//textarea[@placeholder = 'Описание товара']")
    PRICE = (By.XPATH, ".//input[@placeholder = 'Стоимость']")
    DROP_CATEGORY = (By.XPATH, ".//input[@name='category']/following-sibling::button")
    DROP_CITY = (By.XPATH, ".//input[@name='city']/following-sibling::button")
    CITY = (By.XPATH, ".//button[.//span[text()='Санкт-Петербург']]")
    CATEGORY = (By.XPATH, ".//button[.//span[text()='Технологии']]")
    RADIOBATTON = (By.XPATH, ".//input[@value='Б/У']/following-sibling::div[contains(@class, 'radioUnput_inputRegular')]")
    PUBLICATE_BUTTON = (By.XPATH, ".//button[contains(text(), 'Опубликовать')]")
    ADVERTISMENT = (By.XPATH, ".//div[@class= 'about']/h2[text()='Объявление для теста']")
    SEARCH_INPUT = (By.XPATH,".//input[@placeholder='Я хочу купить...']")
