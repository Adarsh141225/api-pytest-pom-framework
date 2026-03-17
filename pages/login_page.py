from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # These are Locators. We keep the names clear and uppercase (standard practice).
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # PROFESSIONAL CHANGE: We use a generic name like 'execute_login' or 'user_login'
    def execute_login(self, username, password):
        """
        Performs a complete login flow.
        This name is professional and doesn't mention the website name.
        """
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)