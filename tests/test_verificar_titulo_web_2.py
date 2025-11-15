# metodo al que se le pasa el navegador que creamos en el conftest
from allure_pytest.utils import pytest_markers

import pytest

from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#aca pytest se usa para indicar cuales test van a ser de smoke
#se ejecuta por consola pytest -s tests/ -m smoke
@pytest.mark.smoke
def test_verificar_titulo_web (driver):
    url="https://www.selenium.dev"
    print(f"Navegando a: {url}")
    driver.get(url)


    #Espera hasta que el titulo contenga Selenium
    WebDriverWait(driver,10).until(EC.title_contains("Selenium"))

    #afirmacion que entre al sitio Selenium
    #Los mensajes salen si falla el assert, si es correcto el assert NO SE muestra el mensaj
    assert "Selenium" in driver.title,"No lo Encontro al titulo"


#Esto es para saltear un test cuando esta en desarrollo
#@pytest.mark.skip("Este test esta en desarrollo, se va a skipear, por ahora falla")
def test_verificar_Pagina_web(driver):
    url="https://www.selenium.dev"
    print(f"URL Site: {url} ")
    # 1. Navegar
    driver.get(url)

    #Espera hasta  que el titulo contenga "Selenium"

    WebDriverWait(driver,10).until(EC.url_contains(url))
    #time.sleep(5)

    # 2. Afirmar(Assert)
    assert "https://www.selenium.dev" in driver.current_url,"No la encontró"