from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    #Constructor de la BasePage, se ejecuta automaticamente al crear un objeto de la clase y es para usar
    #edge en este caso, y poder usarlo en todos los metodos
    #Constructor de la clase BasePage. Se ejecuta automáticamente al crear un objeto de la clase.
    #:param driver: El controlador de Selenium (Chrome, Firefox, Edge, etc.)""
    def __init__(self,driver):
        # Guardamos el navegador activo en 'self.driver' para que todos
        #los métodos puedan usarlo
        self.driver=driver
        # Crea una espera explícita de 10 segundos para evitar errores de timing.
        # Permite que métodos como click(), send_keys() y get_text() esperen que
        # los elementos estén listos antes de interactuar.
        self.wait = WebDriverWait(driver, 10)


    #PORQUE SE PASA EL by Y NO EL LOCATOR SOLAMENTE???????
    def click(self, by, locator):
        element=self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def send_keys(self, by, locator, text):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        #Devuelve el texto de un elemento una vez que es visible.
        return self.wait.until (EC.visibility_of_element_located((by, locator))).text


    def is_visibly(self, by, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except:
            return False

    def current_url(self, by, locator):
       return self.wait.until(EC.visibility_of_element_located((by, locator)))