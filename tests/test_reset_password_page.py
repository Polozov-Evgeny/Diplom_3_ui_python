from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from test_data import helpers
import allure


class TestResetPasswordPage:

    @allure.title('Клик по кнопке "глаз" у пароля делает поле активным — подсвечивает его')
    def test_password_field_highlight(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.enter_email_and_click_recovery_button(helpers.generate_user_data()['email'])
        attribute_password = reset_password_page.click_on_eye_and_get_attribute_password()

        assert 'status_active' in attribute_password
