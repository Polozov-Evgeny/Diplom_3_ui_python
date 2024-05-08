from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
import allure


class HeaderPage(BasePage):

    @allure.step('Нажимаем на ссылку "Конструктор"')
    def click_constructor_link(self):
        self.is_invisible_element(HeaderPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(HeaderPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Нажимаем на ссылку "Лента Заказов"')
    def click_order_feed_link(self):
        self.is_invisible_element(HeaderPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(HeaderPageLocators.ORDER_FEED_LINK)

    @allure.step('Нажимаем на ссылку "Личный кабинет"')
    def click_personal_area_link(self):
        self.is_invisible_element(HeaderPageLocators.LOADING_ANIMATION)
        self.click_on_element_with_wait(HeaderPageLocators.PERSONAL_AREA_LINK)
