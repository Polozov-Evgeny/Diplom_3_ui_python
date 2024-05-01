from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    FIRST_ORDER_NUMBER = [By.XPATH, '//ul[contains(@class,"OrderHistory")]//div[contains(@class,"OrderHistory_textBox")]//'
                                   'p[@class = "text text_type_digits-default"]']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
