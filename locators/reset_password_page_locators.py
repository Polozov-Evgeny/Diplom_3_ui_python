from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    PASSWORD_INPUT = [By.XPATH, '//input[@type = "password"]']
    SAVE_BUTTON = [By.XPATH, '//button[text() = "Сохранить"]']
    EYE_BUTTON = [By.XPATH, '//div[contains(@class, "input__icon")]']
    PASSWORD_DIV = [By.XPATH, '//input[@name = "Введите новый пароль"]/parent::div']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
