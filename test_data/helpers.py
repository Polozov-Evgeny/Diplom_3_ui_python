import requests
from test_data.data import TestData
from faker import Faker
from config.urls import Urls
from config.endpoints import Endpoints
import random
import allure


@allure.step('Генерация данных пользователя')
def generate_user_data():
    fake = Faker()
    user_data = {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.name()
    }
    return user_data


@allure.step('Регистрация нового пользователя через API и возвращение данных для авторизации')
def register_new_user_and_return_login_data():
    registration_data = generate_user_data()
    url = f'{Urls.MAIN_URL}{Endpoints.CREATE_USER_ACCOUNT}'
    response = requests.post(url, data=registration_data)
    if response.status_code == 200 and response.json()['success'] == True:
        login_data = {
            'email': registration_data['email'],
            'password': registration_data['password']
        }
        return login_data
    else:
        print('Проблема с регистрацией пользовательского аккаунта')


@allure.step('Авторизация пользователя через API и возвращение токенов')
def login_user_and_return_tokens(login_data):
    url = f'{Urls.MAIN_URL}{Endpoints.LOGIN_USER}'
    response = requests.post(url, data=login_data)
    if response.status_code == 200 and response.json()['success'] == True:
        login_tokens = {
            'accessToken': response.json()['accessToken'],
            'refreshToken': response.json()['refreshToken']
        }
        return login_tokens
    else:
        print('Проблема с авторизацией пользователя')


@allure.step('Удаление учетной записи пользователя через API')
def delete_user_account(access_token):
    url = f'{Urls.MAIN_URL}{Endpoints.DELETE_USER_ACCOUNT}'
    response = requests.delete(url, headers={'Authorization': access_token})
    if not (response.status_code == 202 and response.json()['success'] == True):
        print('Проблема с удалением пользовательского аккаунт')


@allure.step('Определение случайного id ингридиента через API')
def random_ingredient_id():
    url = f'{Urls.MAIN_URL}{Endpoints.GET_INGREDIENTS}'
    response = requests.get(url)
    ingredient_id = response.json()['data'][random.randint(0, len(response.json()['data']) - 1)]['_id']
    return ingredient_id


@allure.step('Определение случайного id булки для заказа')
def random_bun_id():
    return random.choice(TestData.BUN_ID_LIST)


@allure.step('Создание заказа через API')
def create_order_api(access_token):
    url = f'{Urls.MAIN_URL}{Endpoints.CREATE_ORDER}'
    ingredient_list = [random_bun_id(), random_ingredient_id()]
    headers = {'Authorization': access_token}
    payload = {'ingredients': ingredient_list}
    with allure.step('Отправка запроса на создание заказа пользователя'):
        response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()['order']['number']
    else:
        print('Проблема с созданием ордера пользователя через api')
