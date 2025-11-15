import pytest
import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.helpers import take_screenshot

@allure.feature("Cuenta")
@allure.story("Login Success del usuario")
@pytest.mark.parametrize("user, password, expected_url", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
])
def test_successful_login(navegador, user, password, expected_url):
    with allure.step("1. Iniciar sesión con usuario estándar"):
     login_page = LoginPage(navegador)
     # **Arrange & Act (Usa el Page Object)**
     login_page.login(user, password)

    # **Assert (En el script de prueba)**
    with allure.step("2.Ingresar a Home"):
     home_page = HomePage(navegador)
     current_title = home_page.get_current_title_url()

    browser_name = "firefox"

    # Definir el nombre del navegador que se usará en el screenshot
    if browser_name.lower() == "edge":
        screenshot_browser = "edge"
    elif browser_name.lower() == "firefox":
        screenshot_browser = "firefox"
    else:
        screenshot_browser = None  # o "otro"

    with allure.step("3. Validar Titulo Home"):
     try:
        assert current_title== "Products2"
     except AssertionError:
         take_screenshot(navegador, f"{user}_error", navegador=screenshot_browser)
         raise
    #assert navegador.current_url == expected_url

@allure.story("Login Failed del usuario")
@pytest.mark.parametrize("user, password, expected_error_message", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),  # Usuario bloqueado
    ("invalid_user", "invalid_pass", "Epic sadface: Username and password do not match any user in this service"),
    # Credenciales inválidas
    ("", "secret_sauce", "Epic sadface: Username is required"),  # Campo faltante
])
def test_failed_login(navegador, user, password, expected_error_message):
    with allure.step("1. Iniciar sesión con usuario estándar"):
     login_page = LoginPage(navegador)

     # **Arrange & Act (Usa el Page Object)**
     login_page.login(user, password)

     # **Assert (En el script de prueba)**
     error_text = login_page.get_error_message()  # Obtiene el texto del error usando un getter del PO


    browser_name = "firefox"

    # Definir el nombre del navegador que se usará en el screenshot
    if browser_name.lower() == "edge":
        screenshot_browser = "edge"
    elif browser_name.lower() == "firefox":
        screenshot_browser = "firefox"
    else:
        screenshot_browser = None  # o "otro"

    with allure.step("2. Validar mensaje de error"):
     try:
       assert error_text == expected_error_message  # Verifica que el mensaje de error sea el correcto
     except Exception:
       take_screenshot(navegador, f"{user}_error")
       raise