from selenium.webdriver.common.by import By

from pages.base_page import BasePage

#Pasamos la clase Base para poder usar los metodos definidos ahi
class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        #self es una convención en Python que representa la instancia actual del objeto.
        #Cuando usas self.algo, estás accediendo a un atributo o metodo que fue definido dentro de la clase.
        #El asterisco * es el operador de desempaquetado. Si self.USERNAME_INPUT es una tupla,
        #por ejemplo ('id', 'username'), entonces *self.USERNAME_INPUT la convierte en dos argumentos separados.
        self.send_keys(*self.USERNAME_INPUT, text=username)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

