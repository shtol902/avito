from selenium.webdriver.common.by import By

class MainPageLocators():
    GAME_CARDS = (By.XPATH, "//div[@class='ant-spin-nested-loading css-17a39f8']//li[1]")
    PAGINATION_NEXT = (By.XPATH, "//body//div[@id='root']//div//div[1]//ul[1]//li[9]//button[1]")
    DROPDOWN_BUTTON_20 = (By.CSS_SELECTOR, "#rc_select_3_list_1 > div")
    DROPDOWN = (By.CSS_SELECTOR, "#root > div > div.ant-list.ant-list-split.ant-list-something-after-last-item.css"
                                 "-17a39f8 > div:nth-child(1) > ul > li.ant-pagination-options > div > "
                                 "div.ant-select-selector > span.ant-select-selection-item")
    SECOND_PAGE = (By.CSS_SELECTOR, "#root > div > div.ant-list.ant-list-split.ant-list-something-after-last-item.css"
                                    "-17a39f8 > div:nth-child(1) > ul > li.ant-pagination-item.ant-pagination-item-2")