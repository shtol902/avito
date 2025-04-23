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

    @allure.step("Клик на раскрывающийся список")
    def click_to_dropdown(self):
        self.click_element(MainPageLocators.DROPDOWN)

    @allure.step("Клик на кнопку 20/page в выпадающем списке")
    def click_to_dropdown_item(self):
        self.click_element(MainPageLocators.DROPDOWN_BUTTON_20)

    @allure.step("Получить class элемента")
    def get_class_element(self):
        return self.get_class(MainPageLocators.SECOND_PAGE)

    @allure.step("Получить title элемента")
    def get_title_element(self):
        return self.get_title(MainPageLocators.DROPDOWN)


