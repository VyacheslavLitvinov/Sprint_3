from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP


def test_transition_section_constructor_sauce_success():
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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.user_sauce))

    element_sauce = driver.find_element(*MP.user_sauce)
    driver.execute_script(MP.scroll, element_sauce)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MP.user_sauce))

    transition_sauce = driver.find_element(*MP.active_element_constructor)
    assert transition_sauce.text == 'Соусы'

    driver.quit()


def test_transition_section_constructor_fillings_success():
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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.user_fillings))

    element_fillings = driver.find_element(*MP.user_fillings)
    driver.execute_script(MP.scroll, element_fillings)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MP.user_fillings))

    transition_fillings = driver.find_element(*MP.active_element_constructor)
    assert transition_fillings.text == 'Начинки'

    driver.quit()


def test_transition_section_constructor_loaf_success():
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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(MP.user_loaf))

    driver.find_element(*MP.fillings).click()

    element_loaf = driver.find_element(*MP.user_loaf)
    driver.execute_script(MP.scroll, element_loaf)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MP.user_loaf))

    transition_loaf = driver.find_element(*MP.active_element_constructor)
    assert transition_loaf.text == 'Булки'

    driver.quit()
