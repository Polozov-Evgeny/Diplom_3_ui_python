from pages.header_page import HeaderPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
import allure


class TestHeaderPage:

    @allure.title('Проверка перехода на Главную страницу/Конструктор по клику на "Конструктор"')
    def test_go_to_constructor_page_by_clicking_constructor_link(self, driver):
        header_page = HeaderPage(driver)
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_order_feed_page()
        header_page.click_constructor_link()

        assert constructor_page.check_page()


    @allure.title('Проверка перехода на Ленту заказов по клику на "Лента Заказов"')
    def test_go_to_order_feed_page_by_clicking_order_feed_link(self, driver):
        header_page = HeaderPage(driver)
        order_feed_page = OrderFeedPage(driver)
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_constructor_page()
        header_page.click_order_feed_link()

        assert order_feed_page.check_page()
