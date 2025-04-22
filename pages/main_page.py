import random
import allure
from base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик на кнопку Перейти в кабинет")
    def click_on_card(self):
        self.click_element(MainPageLocators.GAME_CARDS)

    def open_game_card(self):
        cards = self.find_elements(MainPageLocators.GAME_CARDS)
        cards.click()
        return GamePage(self.driver)

    def get_games_count(self):
        return len(self.find_elements(MainPageLocators.GAME_CARDS))

    def go_to_next_page(self):
        self.click(MainPageLocators.PAGINATION_NEXT)
        return self

    def filter_by_genre(self, genre):
        self.find_element(MainPageLocators.GENRE_FILTER).send_keys(genre)
        return self

    def search_game(self, query):
        self.find_element(MainPageLocators.SEARCH_INPUT).send_keys(query)
        self.click(MainPageLocators.SEARCH_BUTTON)
        return self