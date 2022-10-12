from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP
from locators_page import RegistrationPage as RP
from locators_page import ForgotPage as FP


def test_authorization_on_main_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.auth_button_main))

    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.fld_email))

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.order_button))

    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    driver.quit()


def test_authorization_on_private_office_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.fld_private))

    button_private = driver.find_element(*MP.fld_private)
    button_private.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.fld_email))

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.order_button))

    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    driver.quit()


def test_authorization_on_registration_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.fld_private))

    button_private = driver.find_element(*MP.fld_private)
    button_private.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.reg_button))

    button_registration = driver.find_element(*LP.reg_button)
    button_registration.click()

    auth_button_reg = driver.find_element(*RP.auth_button_reg)
    auth_button_reg.click()

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.order_button))

    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    driver.quit()


def test_authorization_on_recovery_page_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.fld_private))

    button_private = driver.find_element(*MP.fld_private)
    button_private.click()

    button_recovery = driver.find_element(*LP.rec_button)
    button_recovery.click()

    driver.find_element(*FP.auth_button_forgot).click()

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.order_button))

    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    driver.quit()
