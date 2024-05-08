from pages.personal_area_page import PersonalAreaPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from test_data import helpers
import allure


class TestOrderFeedPage:

    @allure.title('Проверка открытия всплывающего окна с деталями, если кликнуть на заказ')
    def test_open_order_detail_modal_window_by_clicking_on_order(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        order_feed_page.click_last_order()

        assert order_feed_page.check_open_order_detail_modal_window()


    @allure.title('Проверка, что заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_user_orders_are_in_history_and_feed(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        helpers.create_order_api(access_token)
        personal_area_page = PersonalAreaPage(driver)
        personal_area_page.go_to_personal_area_page()
        personal_area_page.click_order_history_link()
        order_history_page = OrderHistoryPage(driver)
        history_order_number = order_history_page.get_order_number()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        feed_order_number = order_feed_page.get_order_number()

        assert history_order_number == feed_order_number


    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_completed_for_all_time_counter(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        counter_before_order = int(order_feed_page.get_completed_for_all_time_counter())
        helpers.create_order_api(access_token)
        counter_after_order = int(order_feed_page.get_completed_for_all_time_counter())

        assert (counter_after_order - counter_before_order == 1)


    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_executed_today_counter(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        counter_before_order = int(order_feed_page.get_executed_today_counter())
        helpers.create_order_api(access_token)
        counter_after_order = int(order_feed_page.get_executed_today_counter())

        assert (counter_after_order - counter_before_order == 1)


    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_in_the_work_list(self, driver, login_new_user):
        access_token = login_new_user['accessToken']
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        order_number = str(helpers.create_order_api(access_token))
        order_number_in_the_work_list = order_feed_page.get_order_number_in_the_work_list()

        assert order_number in order_number_in_the_work_list