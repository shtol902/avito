from selenium.webdriver.common.by import By

class MainPageLocators():
    GAME_CARDS = (By.XPATH, "//div[@class='ant-spin-nested-loading css-17a39f8']//li[1]")
    FIRST_GAME_TITLE = (By.CSS_SELECTOR, "")
    PAGINATION_NEXT = (By.CSS_SELECTOR, "")
    GENRE_FILTER = (By.CSS_SELECTOR, "")
    SEARCH_INPUT = (By.CSS_SELECTOR, "")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "")