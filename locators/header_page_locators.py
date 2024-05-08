from selenium.webdriver.common.by import By


class HeaderPageLocators:

    PERSONAL_AREA_LINK = [By.XPATH, '//p[text() = "Личный Кабинет"]']
    CONSTRUCTOR_LINK = [By.XPATH, '//p[text() = "Конструктор"]']
    ORDER_FEED_LINK = [By.XPATH, '//p[text() = "Лента Заказов"]']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
