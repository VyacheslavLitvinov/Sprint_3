from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP


def test_transition_from_private_office_in_constructor_success():
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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.constructor_button))

    constructor = driver.find_element(*MP.constructor_button)
    constructor.click()

    assert driver.find_element(*MP.cook_burger).text == 'Соберите бургер'

    driver.quit()


def test_transition_from_private_office_in_constructor_through_burger_button_success():
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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.burger_button))

    burger_button = driver.find_element(*MP.burger_button)
    burger_button.click()

    assert driver.find_element(*MP.cook_burger).text == 'Соберите бургер'

    driver.quit()
