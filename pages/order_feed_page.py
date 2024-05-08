from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from config.urls import Urls
import allure


class OrderFeedPage(BasePage):

    @allure.step(f'Открываем страницу Ленты заказов')
    def go_to_order_feed_page(self):
        self.go_to_url(Urls.ORDER_FEED_URL)

    @allure.step(f'Проверяем открытие страницы Ленты заказов')
    def check_page(self):
        return self.check_open_page(Urls.ORDER_FEED_URL, OrderFeedPageLocators.ORDER_FEED_TEXT)

    @allure.step('Кликаем на последний заказ в списке')
    def click_last_order(self):
        self.is_invisible_element(OrderFeedPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(OrderFeedPageLocators.LAST_ORDER)

    @allure.step('Проверяем наличие модального окна с деталями заказа')
    def check_open_order_detail_modal_window(self):
        return self.is_element_displayed_with_wait(OrderFeedPageLocators.ORDER_COMPOSITION_TEXT)

    @allure.step('Получаем номер последнего заказа в ленте')
    def get_order_number(self):
        return self.get_text_from_element_with_wait(OrderFeedPageLocators.LAST_ORDER_NUMBER)

    @allure.step('Получаем значение счетчика "Выполнено за все время"')
    def get_completed_for_all_time_counter(self):
        return self.get_text_from_element_with_wait(OrderFeedPageLocators.COMPLETED_FOR_ALL_TIME_COUNTER)

    @allure.step('Получаем значение счетчика "Выполнено за сегодня"')
    def get_executed_today_counter(self):
        return self.get_text_from_element_with_wait(OrderFeedPageLocators.EXECUTED_TODAY_COUNTER)

    @allure.step('Ожидаем и получаем отображение номера заказа "В работе"')
    def get_order_number_in_the_work_list(self):
        if self.wait_until_text_changes(OrderFeedPageLocators.IN_THE_WORK_LIST, 'Все текущие заказы готовы!'):
            return self.get_text_from_element_with_wait(OrderFeedPageLocators.IN_THE_WORK_LIST)
        else:
            return print(f'Проблема: отображается {OrderFeedPageLocators.IN_THE_WORK_LIST}')
