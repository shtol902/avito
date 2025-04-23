import random
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик на кнопку Перейти в кабинет")
    def click_on_card(self):
        self.click_element(MainPageLocators.GAME_CARDS)

    @allure.step("Клик на кнопку Вперед в пагинации")
    def click_to_next_page(self):
        self.click_element(MainPageLocators.PAGINATION_NEXT)

    @allure.step("Получить class элемента")
    def get_class_element(self):
        return self.get_class(MainPageLocators.SECOND_PAGE)

    def open_game_card(self):
        cards = self.find_elements(MainPageLocators.GAME_CARDS)
        cards.click()
        return GamePage(self.driver)

    def get_games_count(self):
        return len(self.find_elements(MainPageLocators.GAME_CARDS))


    def filter_by_genre(self, genre):
        self.find_element(MainPageLocators.GENRE_FILTER).send_keys(genre)
        return self
