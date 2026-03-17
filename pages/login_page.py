from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")


    def execute_login(self, username, password):
        """
        Performs a complete login flow.
        This name is professional and doesn't mention the website name.
        """
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)