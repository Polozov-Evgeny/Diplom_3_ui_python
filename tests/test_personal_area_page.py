from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.personal_area_page import PersonalAreaPage
from pages.order_history_page import OrderHistoryPage
import allure


class TestPersonalAreaPage:

    @allure.title('Проверка перехода в профиль по кнопке "Личный Кабинет"')
    def test_go_to_profile_page_by_clicking_personal_area_button(self, driver, login_new_user):
        header_page = HeaderPage(driver)
        personal_area_page = PersonalAreaPage(driver)
        header_page.click_personal_area_link()

        assert personal_area_page.check_page()


    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_go_to_order_history_page_by_clicking_order_history_link(self, driver, login_new_user):
        personal_area_page = PersonalAreaPage(driver)
        order_history_page = OrderHistoryPage(driver)
        personal_area_page.go_to_personal_area_page()
        personal_area_page.click_order_history_link()

        assert order_history_page.check_page()


    @allure.title('Проверка разлогина юзера по кнопке "Выход"')
    def test_logout_by_clicking_exit_link(self, driver, login_new_user):
        personal_area_page = PersonalAreaPage(driver)
        login_page = LoginPage(driver)
        personal_area_page.go_to_personal_area_page()
        personal_area_page.click_exit_link()

        assert login_page.check_page()
