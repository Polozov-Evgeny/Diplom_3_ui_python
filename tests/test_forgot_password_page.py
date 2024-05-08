from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from test_data import helpers
import allure


class TestForgotPasswordPage:

    @allure.title('Проверка перехода на страницу Восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_password_recovery_page_by_clicking_recover_password_button(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        login_page.go_to_login_page()
        login_page.click_restore_password_link()

        assert forgot_password_page.check_page()


    @allure.title('Проверка ввода почты и работа кнопки "Восстановить" на странице Восстановления пароля')
    def test_recovery_button_functionality(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.enter_email_and_click_recovery_button(helpers.generate_user_data()['email'])

        assert reset_password_page.check_page()
