from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import LoginPage as LP
from locators_page import RegistrationPage as RP


def test_registration_valid_data_success(generate_valid_password, generate_email):
    driver = webdriver.Chrome()

    # Переходим на сайт
    driver.get(LP.url_login)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.reg_button))

    # Находим кнопку регистрации и нажимаем на нее
    registration_button = driver.find_element(*LP.reg_button)
    registration_button.click()

    # Заполняем поля имя, email и пароль
    name_field = driver.find_element(*RP.fld_name)
    name_field.send_keys('Александр')
    email_field = driver.find_element(*RP.fld_email)
    email_field.send_keys(generate_email)
    password_field = driver.find_element(*RP.fld_pass)
    password_field.send_keys(generate_valid_password)

    # Нажимаем на кнопку зарегистрироваться
    registration_button = driver.find_element(*RP.reg_button)
    registration_button.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.log_fld))

    # Проверяем, что выполнен переход и отображается поле "Вход"
    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'

    # Выходим из браузера
    driver.quit()


def test_registration_valid_data_url_login(generate_valid_password, generate_email):
    driver = webdriver.Chrome()

    # Переходим на сайт
    driver.get(LP.url_login)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.reg_button))

    # Находим кнопку регистрации и нажимаем на нее
    registration_button = driver.find_element(*LP.reg_button)
    registration_button.click()

    # Заполняем поля имя, email и пароль
    name_field = driver.find_element(*RP.fld_name)
    name_field.send_keys('Александр')
    email_field = driver.find_element(*RP.fld_email)
    email_field.send_keys(generate_email)
    password_field = driver.find_element(*RP.fld_pass)
    password_field.send_keys(generate_valid_password)

    # Нажимаем на кнопку зарегистрироваться
    registration_button = driver.find_element(*RP.reg_button)
    registration_button.click()

    assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    # Выходим из браузера
    driver.quit()


def test_registration_password_less_six_symbol_error(generate_email, generate_not_valid_password):
    driver = webdriver.Chrome()

    # Переходим на сайт
    driver.get(LP.url_login)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.reg_button))

    # Находим кнопку регистрации и нажимаем на нее
    registration_field = driver.find_element(*LP.reg_button)
    registration_field.click()

    # Заполняем поля имя, email и пароль
    name_field = driver.find_element(*RP.fld_name)
    name_field.send_keys('Алёна')
    email_field = driver.find_element(*RP.fld_email)
    email_field.send_keys(generate_email)
    password_field = driver.find_element(*RP.fld_pass)
    password_field.send_keys(generate_not_valid_password)

    # Нажимаем на кнопку зарегистрироваться
    registration_button = driver.find_element(*RP.reg_button)
    registration_button.click()

    error_name = driver.find_element(*RP.err_fld).text
    # Проверяем, что отображается валидация, переход не выполнен
    assert error_name == 'Некорректный пароль'

    # Выходим из браузера
    driver.quit()


def test_registration_password_less_six_symbol_url_register(generate_email, generate_not_valid_password):
    driver = webdriver.Chrome()

    # Переходим на сайт
    driver.get(LP.url_login)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.reg_button))

    # Находим кнопку регистрации и нажимаем на нее
    registration_field = driver.find_element(*LP.reg_button)
    registration_field.click()

    # Заполняем поля имя, email и пароль
    name_field = driver.find_element(*RP.fld_name)
    name_field.send_keys('Алёна')
    email_field = driver.find_element(*RP.fld_email)
    email_field.send_keys(generate_email)
    password_field = driver.find_element(*RP.fld_pass)
    password_field.send_keys(generate_not_valid_password)

    # Нажимаем на кнопку зарегистрироваться
    registration_button = driver.find_element(*RP.reg_button)
    registration_button.click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    # Выходим из браузера
    driver.quit()