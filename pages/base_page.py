from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_and_find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_and_find_elements(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()