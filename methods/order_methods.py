import allure
import requests
from urls import CREATE_ORDER_ENDPOINT, INGREDIENTS_ENDPOINT


class OrderMethods:

    @allure.step("Получение заказов пользователя")
    def get_orders(self, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.get(f'{CREATE_ORDER_ENDPOINT}', headers=headers)
        return response

    @allure.step("Создание заказа")
    def create_order(self, payload, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.post(f'{CREATE_ORDER_ENDPOINT}', json=payload, headers=headers)
        return response

    @allure.step("Получение ингредиентов")
    def get_ingredients(self):
        response = requests.get(f'{INGREDIENTS_ENDPOINT}')
        return response.json()
