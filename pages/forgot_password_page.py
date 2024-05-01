from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from config.urls import Urls
import allure


class ForgotPasswordPage(BasePage):

    def go_to_forgot_password_page(self):
        self.go_to_url(Urls.FORGOT_PASSWORD_URL)

    def check_page(self):
        return self.check_open_page(Urls.FORGOT_PASSWORD_URL, ForgotPasswordPageLocators.RESTORE_BUTTON)

    @allure.step('Вводим email и наживаем кнопку "Восстановить"')
    def enter_email_and_click_recovery_button(self, email):
        self.is_invisible_element(ForgotPasswordPageLocators.LOADING_ANIMATION)
        self.set_text_to_element_with_wait(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click_on_element_with_wait(ForgotPasswordPageLocators.RESTORE_BUTTON)
