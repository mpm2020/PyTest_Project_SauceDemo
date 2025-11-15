import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_home_success(navegador):
    try:
        # Inicializa la página de login
        login_page = LoginPage(navegador)

        # Realiza login
        login_page.login("standard_user", "secret_sauce")

        # Inicializa la página home y obtiene el título o URL actual
        home_page = HomePage(navegador)
        current_url = home_page.get_current_title_url()

        # Validación de login exitoso
        assert current_url == "Products"
        print(f"Login exitoso, página obtenida: {current_url}")

    except AssertionError as ae:
        # Captura errores de validación
        print(f"Error de validación: {ae}")
        pytest.fail(f"Test falló: {ae}")

    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error durante login/HomePage: {e}")
        pytest.fail(f"Error inesperado: {e}")
