import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators_page import MainPage as MP
from locators_page import LoginPage as LP
from selenium.webdriver.common.by import By


def test_transition_section_constructor_success():
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

    element_sauce = driver.find_element(By.XPATH, '//img[@alt= "Соус фирменный Space Sauce"]')
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", element_sauce)
    time.sleep(1)
    transition_sauce = driver.find_element(By.XPATH, '//div[@class= "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]//*')
    assert transition_sauce.text == 'Соусы'

    element_fillings = driver.find_element(By.XPATH, '//img[@alt= "Сыр с астероидной плесенью"]')
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", element_fillings)
    time.sleep(1)
    transition_fillings = driver.find_element(By.XPATH, '//div[@class= "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]//*')
    assert transition_fillings.text == 'Начинки'

    element_loaf = driver.find_element(By.XPATH, '//img[@alt= "Флюоресцентная булка R2-D3"]')
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView();", element_loaf)
    time.sleep(1)
    transition_loaf = driver.find_element(By.XPATH, '//div[@class= "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]//*')
    assert transition_loaf.text == 'Булки'

    driver.quit()
