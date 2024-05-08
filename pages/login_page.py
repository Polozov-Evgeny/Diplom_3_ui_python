from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config.urls import Urls
import allure


class LoginPage(BasePage):

    @allure.step(f'Открываем страницу Авторизации')
    def go_to_login_page(self):
        self.go_to_url(Urls.LOGIN_URL)

    @allure.step('Нажимаем на ссылку "Восстановить пароль"')
    def click_restore_password_link(self):
        self.is_invisible_element(LoginPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(LoginPageLocators.RESTORE_PASSWORD_LINK)


    @allure.step(f'Проверяем открытие страницы Авторизации')
    def check_page(self):
        return self.check_open_page(Urls.LOGIN_URL, LoginPageLocators.LOGIN_BUTTON)
