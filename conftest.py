import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver(self):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://makarovartem.github.io/frontend-avito-tech-test-assignment/")
    yield driver
    driver.quit()