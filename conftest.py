import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from .locators import LoginPageLocators
import random
from faker import Faker
from .config import Url
from .locators import LoginPageLocators, RegistrationPageLocators, AuthorizationPageLocators


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver:WebDriver):
    return WebDriverWait(driver, 5)

@pytest.fixture
def go_to_registration_page(driver:WebDriver, wait):
    driver.get(Url.MAIN_URL)
    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.NO_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT))

@pytest.fixture
def go_to_authorization_page(driver:WebDriver, wait):
    driver.get(Url.MAIN_URL)
    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
    wait.until(expected_conditions.element_to_be_clickable(AuthorizationPageLocators.EMAIL_INPUT))

@pytest.fixture
def create_unique_email():
        return f"user_{random.randint(1000, 9999)}@example.com"

@pytest.fixture
def create_random_description():
        fake = Faker('ru_RU')
        description = fake.text(max_nb_chars=100)
        return description

@pytest.fixture 
def create_random_price():
        return random.randint(1000, 9999)