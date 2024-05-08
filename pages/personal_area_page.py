from pages.base_page import BasePage
from locators.personal_area_page_locators import PersonalAreaPageLocators
from config.urls import Urls
import allure


class PersonalAreaPage(BasePage):

    @allure.step(f'Открываем Личный кабинет')
    def go_to_personal_area_page(self):
        self.go_to_url(Urls.ACCOUNT_URL)

    @allure.step(f'Проверяем открытие страницы с Личным кабинетом')
    def check_page(self):
        return self.check_open_page(Urls.PROFILE_URL, PersonalAreaPageLocators.PROFILE_LINK)

    @allure.step('Нажимаем на ссылку "История заказов"')
    def click_order_history_link(self):
        self.is_invisible_element(PersonalAreaPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(PersonalAreaPageLocators.ORDER_HISTORY_LINK)

    @allure.step('Нажимаем на ссылку "Выход"')
    def click_exit_link(self):
        self.is_invisible_element(PersonalAreaPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(PersonalAreaPageLocators.LOGOUT_BUTTON)
