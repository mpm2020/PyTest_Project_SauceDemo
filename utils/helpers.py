import random
import string
import os

def generar_email_test():
    letras = ''.join(random.choices(string.ascii_lowercase, k=5))
    numero = random.randint(1, 100)
    return f"test{letras}{numero}@mail.com"


def take_screenshot(driver, name, navegador=None):
    """
    Guarda un screenshot en la carpeta 'screenshots' y lo adjunta a Allure.

    Args:
        driver: instancia de Selenium WebDriver.
        name: nombre base del screenshot.
        navegador: nombre del navegador (opcional, ej. 'edge', 'firefox').
    """
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Añadir navegador al nombre si se pasa
    if navegador:
        name = f"{name}_{navegador.lower()}"

    file_path = os.path.join(folder, f"{name}.png")
    driver.save_screenshot(file_path)
    print(f"Screenshot guardado en: {file_path}")