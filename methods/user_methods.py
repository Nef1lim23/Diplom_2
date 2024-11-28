import requests
from data import *
import allure


class UserMethods:
    @allure.step('Создание курьера')
    def post_create_couriers(self, payload):
        r = requests.post(f'{URLs.POST_CREATE_USER}', json=payload)
        return r


    @allure.step('Получение ID курьера')
    def get_id_courier(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        log_in_response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', data=payload)
        return log_in_response.json()['id']

    @allure.step('Авторизация курьера')
    def post_login_courier(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', json=payload)
        return response

    @allure.step('Авторизация курьера без пароля')
    def post_login_courier_without_password(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': ''
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', data=payload)
        return response

    @allure.step('Авторизация курьера без логина')
    def post_login_courier_without_login(self, login_pass):
        payload = {
            'login': '',
            'password': login_pass[1]
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', data=payload)
        return response

