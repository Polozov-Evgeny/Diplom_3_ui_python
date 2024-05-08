from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGIN_BUTTON = [By.XPATH, '//button[text() = "Войти"]']
    RESTORE_PASSWORD_LINK = [By.XPATH, '//a[@href = "/forgot-password"]']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
