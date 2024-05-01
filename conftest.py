import pytest
from selenium import webdriver
from test_data import helpers
from config.urls import Urls
import allure


@pytest.fixture(
    params=[webdriver.Chrome, webdriver.Firefox],
    ids=['chrome', 'firefox'])
def driver(request):
    with allure.step(f'Открываем браузер'):
        driver = request.param()
        driver.maximize_window()
    yield driver
    with allure.step('Закрываем браузер'):
        driver.quit()


@pytest.fixture(scope='function')
def login_new_user(driver):
    new_user = helpers.register_new_user_and_return_login_data()
    tokens = helpers.login_user_and_return_tokens(new_user)
    driver.get(Urls.MAIN_URL)
    token_script = (f'localStorage.setItem("accessToken", "{tokens['accessToken']}");'
                    f'localStorage.setItem("refreshToken", "{tokens['refreshToken']}");')
    driver.execute_script(token_script)
    yield tokens
    helpers.delete_user_account(tokens['accessToken'])
