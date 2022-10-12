from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP
from locators_page import PrivateOffice as PO


def test_transition_personal_area_on_click_have_message():
    driver = webdriver.Chrome()
    driver.maximize_window()

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
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(PO.message))

    assert driver.find_element(*PO.message).text == 'В этом разделе вы можете изменить свои персональные данные'

    driver.quit()


def test_transition_personal_area_on_click_have_button_profile():
    driver = webdriver.Chrome()
    driver.maximize_window()

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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PO.profile))

    assert driver.find_element(*PO.profile).text == 'Профиль'

    driver.quit()


def test_transition_personal_area_on_click_have_button_history():
    driver = webdriver.Chrome()
    driver.maximize_window()

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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PO.history))

    assert driver.find_element(*PO.history).text == 'История заказов'

    driver.quit()


def test_transition_personal_area_on_click_have_button_exit_button():
    driver = webdriver.Chrome()
    driver.maximize_window()

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

    assert driver.find_element(*PO.exit_button).text == 'Выход'

    driver.quit()


def test_transition_personal_area_on_click_url_profile():
    driver = webdriver.Chrome()
    driver.maximize_window()

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
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    driver.quit()
