import pytest

# Se importa el metodo desde utils > helpers para sacar la fotografia
from utils.helpers import take_screenshot

#aca pytest se usa para ejecutar el test con determinados datos
@pytest.mark.parametrize("username,password", [
    ("standard_user","secret_sauce"),
    ("locked_out_user","secret_sauce")
])

def test_login(driver,username,password):
    url="https://www.saucedemo.com"
    print(f"Navegando a: {url}")
    driver.get(url)
    #'id' no todas las versiones lo reconocen, todas aceptan el By.ID
    driver.find_element('id', "user-name").send_keys(username)
    driver.find_element('id', "password").send_keys(password)
    driver.find_element('id', "login-button").click()

    current_url=driver.current_url
    expected_url="inventory.html"

    try:
        assert expected_url in current_url, f"URL inesperada{current_url}"
        print(f"Login exitoso para {username}")
    # Aca sacaria la fotografia, si el test falla, se define en utils > helpers
    except AssertionError:
        #el metodo desde  take_screenshot esta en utils > helpers que se importo,
        # para sacar la fotografiava a fallar con este usuario "locked_out_user","secret_sauce" porque no funciona
        take_screenshot(driver,f"{username}_error")
        #se pone el raise para indicar que el test falla, sino se pone no se marca como que el test falla
        raise
