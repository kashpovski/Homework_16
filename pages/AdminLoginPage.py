from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    PATH = "admin"
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    USER_MENU = (By.CSS_SELECTOR, "li.dropdown")
    HELP_BLOCK = (By.CSS_SELECTOR, ".help-block a")
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")

    def login(self, username="", password=""):
        self._input(self.element(self.USERNAME), username)
        self._input(self.element(self.PASSWORD), password)
        self.browser.find_element(*self.BUTTON_LOGIN).click()
        return self

    def verify_login(self):
        return self.element(self.USER_MENU)

    def verify_help_block(self):
        return self.element(self.HELP_BLOCK)

    def verify_forgotten_password(self):
        self.element(self.HELP_BLOCK).click()
        return self.element(self.EMAIL)
