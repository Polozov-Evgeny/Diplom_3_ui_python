from pages.base_page import BasePage
from locators.personal_area_page_locators import PersonalAreaPageLocators
from locators.order_history_page_locators import OrderHistoryPageLocators
from config.urls import Urls
import allure


class OrderHistoryPage(BasePage):

    @allure.step(f'Проверяем открытие страницы Истории ордеров')
    def check_page(self):
        return self.check_open_page(Urls.ORDER_HISTORY_URL, PersonalAreaPageLocators.PROFILE_LINK)

    @allure.step('Получаем номер первого заказа в истории')
    def get_order_number(self):
        return self.get_text_from_element_with_wait(OrderHistoryPageLocators.FIRST_ORDER_NUMBER)
