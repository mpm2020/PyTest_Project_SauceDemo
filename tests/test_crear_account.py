import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import generar_email_test  # <-- importamos la función que esta en la carpeta utils > helpers
def test_crear_account(driver):
    driver.get("http://automationpractice.pl/index.php?controller=authentication&back=my-account")
    # aca llama al metodo que genera el email random que esta en la carpeta utils > helpers
    email = generar_email_test()
    driver.find_element(By.ID, "email_create").send_keys(email)
    driver.find_element(By.ID, "SubmitCreate").click()