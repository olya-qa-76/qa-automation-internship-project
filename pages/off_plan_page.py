from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class OffPlanPage(Page):
    OFF_PLAN_BTN = (By.XPATH, "//button[text()='Off-plan']")
    SEARCH_AND_FILTERS_BTN = (By.XPATH, "//*[contains(@class,'md:block')]//*[contains(text(),'Search & filters')]")
    ANNOUNCED_BTN = (By.XPATH, "//div[@data-test-id='filter-badge-announced']")
    SHOW_BTN = (By.XPATH, "//button[@data-test-id='all-filters-submit']")
    PROJECT_CARDS = (By.CSS_SELECTOR, "a[data-test-id*='project-card']")

    def verify_off_plan_opens(self):
        self.wait_until_element_present(*self.OFF_PLAN_BTN)

    def filter_by_announced(self):
        self.wait_until_clickable_click(*self.SEARCH_AND_FILTERS_BTN)
        self.scroll_to_element(*self.ANNOUNCED_BTN)
        self.wait_until_clickable_click(*self.ANNOUNCED_BTN)
        self.wait_until_clickable_click(*self.SHOW_BTN)

    def verify_announced(self):
        project_cards = self.driver.find_elements(*self.PROJECT_CARDS)

        assert project_cards, "No project cards found after filtering"

        for index, card in enumerate(project_cards, start=1):
            statuses = card.find_elements(By.XPATH, ".//span[text()='Announced']")
            assert statuses, f"Card #{index} does not contain 'Announced' status"