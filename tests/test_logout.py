import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP
from locators_page import PrivateOffice as PO


def test_logout_from_private_office_success():
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

    logout_button = driver.find_element(*PO.exit_button)
    assert logout_button.text == 'Выход'
    logout_button.click()
    time.sleep(1)

    log_field = driver.find_element(*LP.log_fld)
    assert log_field.text == 'Вход'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()
