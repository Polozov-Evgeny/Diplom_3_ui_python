from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT = [By.XPATH, '//label[text() = "Email"]/parent::div/input']
    RESTORE_BUTTON = [By.XPATH, '//button[text() = "Восстановить"]']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
