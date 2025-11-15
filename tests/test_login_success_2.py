
#navegador lo trae @pytest.fixture(params=["chrome","edge"]), ahi esta definido navegador

def test_login_success(navegador):
    url = "https://www.saucedemo.com"

    #Muestra por consola donde esta navegando
    print (f"1.Navegando a la URL: {url}")

    #Navega a la página
    navegador.get(url)
    navegador.find_element('id',"user-name").send_keys("standard_user")
    navegador.find_element('id', "password").send_keys("secret_sauce")
    navegador.find_element('id', "login-button").click()

    #Imprimir a la página donde llega cuando se loguea por consola
    current_url=navegador.current_url
    print(f"4.Página obtenida: {current_url=}")

    # Confirma la página
    expected_url="inventory.html"
    assert "inventory.html" in expected_url

    print(f"5.Página obtenida exitosa: {current_url=}")