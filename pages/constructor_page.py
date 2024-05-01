from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from config.urls import Urls
import allure


class ConstructorPage(BasePage):

    def go_to_constructor_page(self):
        self.go_to_url(Urls.CONSTRUCTOR_URL)

    def check_page(self):
        return self.check_open_page(Urls.CONSTRUCTOR_URL, ConstructorPageLocators.ASSEMBLE_BURGER_TEXT)

    @allure.step('Определяем локатор случайного ингредитента/его элемента')
    def find_random_ingredient_locator(self, random_ingredient_id, element_locator):
        method, ingredient_locator = element_locator
        ingredient_locator_with_random_id = (method, ingredient_locator.format(ingredient_id=random_ingredient_id))
        return ingredient_locator_with_random_id

    @allure.step('Кликаем по случайному ингридиенту')
    def click_random_ingredient(self, random_ingredient_id):
        ingredient_locator_with_random_id = self.find_random_ingredient_locator(random_ingredient_id,
                                                                                ConstructorPageLocators.RANDOM_INGREDIENT_ITEM)
        self.scroll_to_element(ingredient_locator_with_random_id)
        self.click_on_element_with_wait(ingredient_locator_with_random_id)

    @allure.step('Проверяем наличие модального окна с деталями по соответсвующему ингредиенту')
    def check_open_ingredient_detail_modal_window(self, ingredient_id):
        return (self.is_element_displayed_with_wait(ConstructorPageLocators.INGREDIENT_DETAILS_TEXT)
                and self.check_open_page(Urls.INGREDIENT_CARD_URL.
                                         format(id=ingredient_id), ConstructorPageLocators.INGREDIENT_DETAILS_TEXT))

    @allure.step('Кликаем на "крестик" у модального окна с деталями ингредиента')
    def click_cross_ingredient_detail_modal_window(self):
        self.click_on_element_with_wait(ConstructorPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step('Проверяем отсутствие модального окна с деталями ингредиента')
    def check_close_ingredient_detail_modal_window(self):
        return self.is_invisible_element(ConstructorPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step('Перетаскиваем ингредиента в область сбора заказа')
    def drag_ingredient_to_order_picking_area(self, random_ingredient_id):
        ingredient_locator_with_random_id = self.find_random_ingredient_locator(random_ingredient_id,
                                                                                ConstructorPageLocators.RANDOM_INGREDIENT_ITEM)
        self.scroll_to_element(ingredient_locator_with_random_id)
        self.drag_element_to_another_area(ingredient_locator_with_random_id,
                                          ConstructorPageLocators.ORDER_PICKING_AREA)

    @allure.step('Получаем значение счетчика по ингредиенту добавленному в заказ')
    def get_value_of_ingredient_counter(self, random_ingredient_id):
        ingredient_counter = self.find_random_ingredient_locator(random_ingredient_id,
                                                                 ConstructorPageLocators.INGREDIENT_COUNTER)
        return self.get_text_from_element_with_wait(ingredient_counter)

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_order_button(self):
        self.click_on_element_with_wait(ConstructorPageLocators.ORDER_BUTTON)

    @allure.step('Проверяем отображение успешного модального окна с номером заказа')
    def check_open_success_screen_with_order_number(self):
        if self.wait_until_text_changes(ConstructorPageLocators.ORDER_NUMBER_ON_SUCCESS_SCREEN, '9999'):
            return self.is_element_displayed_with_wait(ConstructorPageLocators.PENDING_ORDER_TEXT)
        else:
            return False
