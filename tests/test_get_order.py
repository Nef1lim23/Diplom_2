import allure

from methods.order_methods import OrderMethods

order_methods = OrderMethods()


class TestGetOrder:

    @allure.title('Получение заказа авторизованным пользователем')
    def test_get_order_for_auth_user(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.get_orders(access_token)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Получение заказа  не авторизованным пользователем')
    def test_get_order_for_not_auth_user(self, create_and_delete_user):
        response = order_methods.get_orders('')
        assert response.status_code == 401 and response.json()['success'] is False

