from pages.base_page import BasePage

from selenium.webdriver.common.by import By

#Pasamos la clase Base para poder usar los metodos definidos ahi
class HomePage(BasePage):
    TITLE_HOME=(By.CSS_SELECTOR,".title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_current_title_url(self):
        return self.current_url(*self.TITLE_HOME).text

    def logout(self):
        self.click(*self.MENU_BUTTON)
        self.click(*self.LOGOUT_LINK)
