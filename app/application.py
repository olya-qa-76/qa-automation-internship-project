from pages.base_page import Page
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.sign_in_page = SignInPage(driver)