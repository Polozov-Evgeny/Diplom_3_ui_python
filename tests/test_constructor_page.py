from pages.constructor_page import ConstructorPage
from test_data import helpers
import allure


class TestConstructorPage:

    @allure.title('Проверка открытия всплывающего окна с деталями, если кликнуть на ингредиент')
    def test_open_ingredient_detail_modal_window_by_clicking_on_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_constructor_page()
        ingredient_id = helpers.random_ingredient_id()
        constructor_page.click_random_ingredient(ingredient_id)

        assert constructor_page.check_open_ingredient_detail_modal_window(ingredient_id)


    @allure.title('Проверка закрытия всплывающего окна с деталями ингридиента, если кликнуть на "крестик"')
    def test_close_ingredient_detail_modal_window_by_clicking_on_cross(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_constructor_page()
        ingredient_id = helpers.random_ingredient_id()
        constructor_page.click_random_ingredient(ingredient_id)
        constructor_page.click_cross_ingredient_detail_modal_window()

        assert constructor_page.check_close_ingredient_detail_modal_window()


    @allure.title('Проверка увеличения счетчика ингредиента при добавлении этого ингредиента в заказ')
    def test_increase_ingredient_counter_when_adding_ingredient_to_order(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_constructor_page()
        ingredient_id = helpers.random_ingredient_id()
        before_ingredient_counter = constructor_page.get_value_of_ingredient_counter(ingredient_id)
        constructor_page.drag_ingredient_to_order_picking_area(ingredient_id)
        after_ingredient_counter = constructor_page.get_value_of_ingredient_counter(ingredient_id)

        assert after_ingredient_counter > before_ingredient_counter


    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_order_creation_by_authorized_user(self, driver, login_new_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_constructor_page()
        bun_id = helpers.random_bun_id()
        ingredient_id = helpers.random_ingredient_id()
        constructor_page.drag_ingredient_to_order_picking_area(bun_id)
        constructor_page.drag_ingredient_to_order_picking_area(ingredient_id)
        constructor_page.click_order_button()

        assert constructor_page.check_open_success_screen_with_order_number()
