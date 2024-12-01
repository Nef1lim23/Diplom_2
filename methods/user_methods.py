import requests
from data import *
import allure


class UserMethods:

    @allure.step("Создание пользователя")
    def post_create_user(self, payload):
        response = requests.post(f'{URLs.POST_CREATE_USER}', json=payload)
        return response

    @allure.step("Авторизация пользователя")
    def post_login_user(self, payload):
        response = requests.post(f'{URLs.LOGIN_USER_URL}', json=payload)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.delete(f'{URLs.DELETE_COURIER_URL}', headers=headers)
        return response
