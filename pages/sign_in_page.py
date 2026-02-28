from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#field")
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")

    def login(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BTN)