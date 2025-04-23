from selenium.webdriver.common.by import By

class MainPageLocators():
    GAME_CARDS = (By.XPATH, "//div[@class='ant-spin-nested-loading css-17a39f8']//li[1]")
    PAGINATION_NEXT = (By.XPATH, "//body//div[@id='root']//div//div[1]//ul[1]//li[9]//button[1]")
    GENRE_FILTER = (By.CSS_SELECTOR, "")
    SECOND_PAGE = (By.CSS_SELECTOR, "#root > div > div.ant-list.ant-list-split.ant-list-something-after-last-item.css-17a39f8 > div:nth-child(1) > ul > li.ant-pagination-item.ant-pagination-item-2")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "")