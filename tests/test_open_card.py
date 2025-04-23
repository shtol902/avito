import pytest
import allure
from urls import Url
from pages.card_page import CardPage
from pages.base_page import BasePage
from pages.main_page import MainPage


@allure.story("Проверка перехода на страницу игры")
@allure.suite("Переходы")
@allure.tag("positive")
def test_redirect_card_page(driver):
    main_page = MainPage(driver)
    driver.get(Url.MAIN_PAGE)
    main_page.click_on_card()
    card_page = CardPage(driver)
    card_page.wait_for_page_loaded('game')
    assert 'game' in card_page.get_url_card_page()
