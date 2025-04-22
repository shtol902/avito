import allure
from pages.base_page import BasePage


class CardPage(BasePage):
    @allure.step("Получить url страницы")
    def get_url_card_page(self):
        return self.get_url_page()

    @allure.step("Ожидание части URL в адресе")
    def wait_for_page_loaded(self, url):
        self.wait_for_url_contains(url)
        return self