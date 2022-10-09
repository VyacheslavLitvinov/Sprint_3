import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP
from locators_page import RegistrationPage as RP
from locators_page import ForgotPage as FP


def test_authorization_on_main_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 10)

    button_main = driver.find_element(*MP.auth_button_main)
    text_button_main = button_main.text
    assert text_button_main == 'Войти в аккаунт'

    button_main.click()
    time.sleep(1)

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()

    time.sleep(1)

    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    driver.quit()


def test_authorization_on_private_office_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 10)

    button_private = driver.find_element(*MP.fld_private)
    text_button_private = button_private.text
    assert text_button_private == 'Личный Кабинет'
    button_private.click()
    time.sleep(1)

    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()

    time.sleep(1)
    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    driver.quit()


def test_authorization_on_registration_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 10)

    button_private = driver.find_element(*MP.fld_private)
    button_private.click()
    time.sleep(1)

    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'

    button_registration = driver.find_element(*LP.reg_button)
    assert button_registration.text == 'Зарегистрироваться'
    button_registration.click()

    reg_field = driver.find_element(*RP.reg_fld)
    assert reg_field.text == 'Регистрация'

    auth_button_reg = driver.find_element(*RP.auth_button_reg)
    assert auth_button_reg.text == 'Войти'
    auth_button_reg.click()

    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    assert button_login.text == 'Войти'
    button_login.click()

    time.sleep(1)
    button_order = driver.find_element(*MP.order_button)

    assert button_order.text == 'Оформить заказ'

    driver.quit()


def test_authorization_on_recovery_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 10)

    button_private = driver.find_element(*MP.fld_private)
    button_private.click()

    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'

    button_recovery = driver.find_element(*LP.rec_button)
    assert button_recovery.text == 'Восстановить пароль'
    button_recovery.click()

    rec_field = driver.find_element(*FP.fld_forgot_password)
    assert rec_field.text == 'Восстановление пароля'
    forgot_button = driver.find_element(*FP.forgot_button)
    assert forgot_button.text == 'Восстановить'

    driver.find_element(*FP.auth_button_forgot).click()

    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    assert button_login.text == 'Войти'
    button_login.click()

    time.sleep(1)
    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    driver.quit()
