from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    ORDER_FEED_TEXT = [By.XPATH, '//h1[text() = "Лента заказов"]']
    LAST_ORDER = [By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//a']
    ORDER_COMPOSITION_TEXT = [By.XPATH, '//p[text() = "Cостав"]']
    LAST_ORDER_NUMBER = [By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//div[contains(@class,"OrderHistory_textBox")]//'
                                   'p[@class = "text text_type_digits-default"]']
    COMPLETED_FOR_ALL_TIME_COUNTER = [By.XPATH, '//p[text() = "Выполнено за все время:"]/following-sibling::p']
    EXECUTED_TODAY_COUNTER = [By.XPATH, '//p[text() = "Выполнено за сегодня:"]/following-sibling::p']
    IN_THE_WORK_LIST = [By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady")]/li']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
