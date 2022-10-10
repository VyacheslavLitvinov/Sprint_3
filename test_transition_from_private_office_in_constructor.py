import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP


def test_transition_from_private_office_in_constructor_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)
    WebDriverWait(driver, 10)

    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()
    time.sleep(1)

    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    button_private = driver.find_element(*MP.fld_private)
    assert button_private.text == 'Личный Кабинет'
    button_private.click()
    time.sleep(1)

    constructor = driver.find_element(*MP.constructor_button)
    assert constructor.text == 'Конструктор'
    constructor.click()

    assert driver.find_element(*MP.cook_burger).text == 'Соберите бургер'

    driver.quit()


def test_transition_from_private_office_in_constructor_through_burger_button_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(MP.url_main)

    WebDriverWait(driver, 10)

    button_main = driver.find_element(*MP.auth_button_main)
    button_main.click()

    email_field = driver.find_element(*LP.fld_email)
    email_field.send_keys(LP.test_email)
    password_field = driver.find_element(*LP.fld_pass)
    password_field.send_keys(LP.test_pass)

    button_login = driver.find_element(*LP.auth_button_login)
    button_login.click()

    time.sleep(1)
    button_order = driver.find_element(*MP.order_button)
    assert button_order.text == 'Оформить заказ'

    button_private = driver.find_element(*MP.fld_private)
    assert button_private.text == 'Личный Кабинет'
    button_private.click()
    time.sleep(1)

    burger_button = driver.find_element(*MP.burger_button)
    burger_button.click()

    assert driver.find_element(*MP.cook_burger).text == 'Соберите бургер'

    driver.quit()
