from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP
from locators_page import PrivateOffice as PO


def test_logout_from_private_office_success():
    driver = webdriver.Chrome()

    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.auth_button_main))

    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.fld_private))

    button_private = driver.find_element(*MP.fld_private)
    button_private.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PO.exit_button))

    logout_button = driver.find_element(*PO.exit_button)
    logout_button.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LP.log_fld))

    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'

    driver.quit()


def test_logout_from_private_office_url_success():
    driver = webdriver.Chrome()

    driver.get(MP.url_main)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.auth_button_main))

    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.fld_private))

    button_private = driver.find_element(*MP.fld_private)
    button_private.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PO.exit_button))

    logout_button = driver.find_element(*PO.exit_button)
    logout_button.click()

    assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    driver.quit()
