from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_and_find_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_and_find_elements(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.wait_and_find_element(locator).click()

    def get_url_page(self):
        return self.driver.current_url

    def get_class(self, locator):
        return self.wait_and_find_element(locator).get_attribute('class')

    def get_title(self, locator):
        return self.wait_and_find_element(locator).get_attribute('title')

    def wait_for_url_contains(self, url_part):
        self.wait.until(EC.url_contains(url_part))
        return self