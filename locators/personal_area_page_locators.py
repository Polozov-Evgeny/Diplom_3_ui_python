from selenium.webdriver.common.by import By


class PersonalAreaPageLocators:

    PROFILE_LINK = [By.XPATH, '//a[text() = "Профиль"]']
    ORDER_HISTORY_LINK = [By.XPATH, '//a[text() = "История заказов"]']
    LOGOUT_BUTTON = [By.XPATH, '//button[text() = "Выход"]']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
