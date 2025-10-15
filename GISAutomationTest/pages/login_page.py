from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "loginField")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.ID, "loginSubmitButton")
    LOGOUT1 = (By.ID, "btn-signInCombo")
    LOGOUT2 = (By.LINK_TEXT, "Log out")

    def open(self, url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.LOGOUT1))
            return True
        except:
            return False
