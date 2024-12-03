import requests
import allure
import helpers
from urls import POST_CREATE_USER, LOGIN_USER_URL, DELETE_COURIER_URL, PATCH_DATA_FOR_USER


class UserMethods:

    @allure.step("Создание пользователя")
    def post_create_user(self, payload):
        response = requests.post(f'{POST_CREATE_USER}', json=payload)
        return response

    @allure.step("Авторизация пользователя")
    def post_login_user(self, payload):
        response = requests.post(f'{LOGIN_USER_URL}', json=payload)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.delete(f'{DELETE_COURIER_URL}', headers=headers)
        return response

    @allure.title('Обновление данных пользователя')
    def patch_data_user(self, access_token):
        headers = {
            'Authorization': access_token
        }
        patch_data = helpers.generate_new_email()
        response = requests.patch(f'{PATCH_DATA_FOR_USER}', headers=headers, data=patch_data)
        return response
