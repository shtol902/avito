import pytest
import allure
from urls import Url
from pages.base_page import BasePage
from pages.main_page import MainPage


@allure.story("Проверка отображение разного количества карточек игр на странице поиска")
@allure.suite("Количество")
@allure.tag("positive")
def test_count_games_on_page(driver):
    main_page = MainPage(driver)
    driver.get(Url.MAIN_PAGE)
    main_page.click_to_dropdown()
    main_page.click_to_dropdown_item()
    assert '20' in main_page.get_title_element()