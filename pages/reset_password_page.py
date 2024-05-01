from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
from config.urls import Urls
import allure


class ResetPasswordPage(BasePage):

    def check_page(self):
        return self.check_open_page(Urls.RESET_PASSWORD_URL, ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Кликаем по кнопке "глаз" и получаем атрибут поля Пароль')
    def click_on_eye_and_get_attribute_password(self):
        self.is_invisible_element(ResetPasswordPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(ResetPasswordPageLocators.EYE_BUTTON)
        return self.get_attribute_element(ResetPasswordPageLocators.PASSWORD_DIV, 'class')
