import allure
from data import VALID_INGREDIENTS_PAYLOAD, EMPTY_INGREDIENTS_PAYLOAD, INVALID_INGREDIENTS_PAYLOAD
from methods.order_methods import OrderMethods

order_methods = OrderMethods()


class TestCreateOrder:

    @allure.title('создание заказа с авторизацией')
    def test_create_order_auth(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.create_order(VALID_INGREDIENTS_PAYLOAD, access_token)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('создание заказа с без авторизации')
    def test_create_order_without_auth(self, create_and_delete_user):
        response = order_methods.create_order(VALID_INGREDIENTS_PAYLOAD, '')
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('создание заказа с без ингредиентов')
    def test_create_without_ing(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.create_order(EMPTY_INGREDIENTS_PAYLOAD, access_token)
        assert response.status_code == 400 and response.json()['success'] is False

    @allure.title('создание заказа с неверным хешем ингредиента')
    def test_invalid_hash_ing(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.create_order(INVALID_INGREDIENTS_PAYLOAD, access_token)
        assert response.status_code == 400 and response.json()['success'] is False
