from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, timeout=10)
        self.base_url = 'https://soft.reelly.io'

    def open_url(self, end_url=''):
        logger.info(f'Opening url: {self.base_url}')
        self.driver.get(f'{self.base_url}{end_url}')

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        logger.info(f'Searching for {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking on {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f"Entering {text} in {locator}")
        self.driver.find_element(*locator).send_keys(text)

    def wait_until_element_present(self, *locator):
        self.driver.wait.until(
            EC.presence_of_element_located(locator),
            message=f'Element not present by locator {locator}'
        )

    def wait_until_all_elements_visible(self, locator):
        self.driver.wait.until(
            EC.visibility_of_all_elements_located(*locator),
            message=f"Elements not visible by locator {locator}"
        )

    def wait_until_element_invisible(self, *locator):
        self.driver.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by locator {locator}'
        )

    def wait_until_clickable(self, locator):
        logger.info(f'Waiting for {locator} to be clickable')
        self.driver.wait.until(
            EC.element_to_be_clickable(*locator),
            message=f"Element not clickable by locator {locator}"
        )

    def wait_until_clickable_click(self, *locator):
        logger.info(f'Waiting and clicking on {locator}')
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by locator {locator}'
        ).click()

    def wait_until_url_contains(self, expected_partial_url):
        self.driver.wait.until(
            EC.url_contains(expected_partial_url),
            message=f"Expected '{expected_partial_url}' not in actual '{self.driver.current_url}'"
        )

    def scroll_to_element(self, *locator):
        element = self.driver.wait.until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def close_page(self):
        self.driver.close()

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text in actual_text,\
            f"Expected '{expected_partial_text}' not in '{actual_text}'"

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text,\
            f"Expected '{expected_text}', but got '{actual_text}'"

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        logger.info(f'Verifying partial URL: {expected_partial_url}')
        assert expected_partial_url in actual_url,\
            f"Expected '{expected_partial_url}' not in actual '{actual_url}'"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url,\
            f"Expected '{expected_url}', but got actual '{actual_url}'"