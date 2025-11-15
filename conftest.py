import pytest
from pyexpat import features
from selenium import webdriver


@pytest.fixture
def driver():
    # Inicia, instala chrome y lo iniciliza
    driver = webdriver.Chrome()

    driver.maximize_window()
    # Pausa y entrega control a la prueba


    yield driver

    # Cierra
    driver.quit()

#El fixture gestiona la creación y destrucción del driver de Selenium.
#Se puede agregar un “scope” para definir la duración del fixture.
#Scopes disponibles:
#- function: antes y después de cada test
#- class: una vez por clase de test
#- module: una vez por archivo de test
# session: una vez por toda la ejecución

#@pytest.fixture(params=["chrome","edge"],scope='function')
@pytest.fixture(params=["firefox"],scope='function')
#request.param es la forma de acceder a chrome o edge
def navegador(request):
    #se pone param y no params, porque se llama chrome o edge
    browser=request.param

    if browser == "firefox":
        navegador = webdriver.Firefox()

    else:
        navegador = webdriver.Edge()


    navegador.maximize_window()
    navegador.get("https://www.saucedemo.com/")

    yield navegador

    navegador.quit()
