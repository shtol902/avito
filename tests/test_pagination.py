import pytest
import allure
from pages.card_page import CardPage
from pages.base_page import BasePage
from pages.main_page import MainPage


@allure.story("Проверка перехода на следующую страницу пагинации")
@allure.suite("Переходы")
@allure.tag("positive")
def test_next_pagination_page(driver):
    main_page = MainPage(driver)
    driver.get('https://makarovartem.github.io/frontend-avito-tech-test-assignment/')
    main_page.click_to_next_page()
    assert 'active' in main_page.get_class_element()