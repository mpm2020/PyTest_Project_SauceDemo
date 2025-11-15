import pytest
import allure

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.helpers import take_screenshot
@allure.feature("Cuenta")
@allure.story("Logout del usuario")
def test_logout(navegador):
    with allure.step("1. Iniciar sesión con usuario estándar"):
     # 1. Login
     login_page = LoginPage(navegador)
     login_page.login("standard_user", "secret_sauce")

    with allure.step("2. Ejecutar logout"):
     # 2. Logout
     home_page = HomePage(navegador)
     home_page.logout()

    with allure.step("3. Validar que volvemos a la página de login"):
     # 3. Validar que volvemos a la página de login
     try:
 c
     except AssertionError:
        take_screenshot(navegador,"logout_error")
        raise



