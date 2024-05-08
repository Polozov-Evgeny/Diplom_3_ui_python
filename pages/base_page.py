from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException, NoSuchElementException
import logging
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def find_visible_element(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.logger.error(f'Элемент {locator} не найден в окне браузера')

    def is_element_displayed_with_wait(self, locator):
        try:
            return self.find_visible_element(locator).is_displayed()
        except (AttributeError, TimeoutException, NoSuchElementException):
            return False

    def is_invisible_element(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(
                expected_conditions.invisibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_until_text_changes(self, locator, old_text):
        try:
            WebDriverWait(self.driver, 5).until_not(
                expected_conditions.text_to_be_present_in_element(locator, old_text))
            return True
        except Exception as e:
            self.logger.error('Проблема:', e)
            return False

    def find_clicable_element(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException):
            self.logger.error(f'Элемент {locator} не найден/не кликабелен')

    def click_on_element_with_wait(self, locator):
        try:
            self.find_clicable_element(locator).click()
        except (AttributeError, TimeoutException, NoSuchElementException):
            self.logger.error(f'Элемент "{locator}" не найден/не кликабелен')

    def set_text_to_element_with_wait(self, locator, text):
        self.find_visible_element(locator).send_keys(text)

    def get_text_from_element_with_wait(self, locator):
        return self.find_visible_element(locator).text

    def scroll_to_element(self, locator):
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_attribute_element(self, locator, attribute):
        element = self.find_visible_element(locator)
        return element.get_attribute(attribute)

    def drag_element_to_another_area(self, element_locator, area_locator):
        element_to_drag = self.find_clicable_element(element_locator)
        area = self.find_clicable_element(area_locator)
        ActionChains(self.driver).drag_and_drop(element_to_drag, area).perform()

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_browser_tab(self, number):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[number])

    def check_open_page(self, expected_url, visible_element_locator):
        with allure.step(f'Проверяем открытие страницы "{expected_url}"'):
            self.is_element_displayed_with_wait(visible_element_locator)
            current_url = self.get_current_url()
            if self.check_result(current_url, expected_url):
                return True
            else:
                print(f'Ошибка: текущий URL [{current_url}] не соответствует ожидаемуму URL [{expected_url}]')
                return False

    @staticmethod
    def check_result(actual_result, expected_result):
        with allure.step(f'Сравниваем фактически полученный результат [{actual_result}] с ожидаемым [{expected_result}]'):
            return actual_result == expected_result
