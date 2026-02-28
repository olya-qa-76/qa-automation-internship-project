from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN_BTN = (By.XPATH, "//li//span[text()='Off-plan']")

    def click_off_plan(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_BTN)