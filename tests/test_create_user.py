import allure
import pytest
from data import *
from methods.user_methods import UserMethods

user_methods = UserMethods()


class TestUserEndpoints:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, create_and_delete_user):
        response = create_and_delete_user['response']
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, create_and_delete_user):
        payload = create_and_delete_user['payload']
        duplicate_response = user_methods.post_create_user(payload)
        assert duplicate_response.status_code == 403 and duplicate_response.json() == DUP_USER_RESPONSE


    @allure.title('создание пользователя без обязательного поля')
    @pytest.mark.parametrize('payload', InvalidDataForRegistration.payloads)
    def test_create_user_without_required_field(self, payload):
        create_courier = UserMethods()
        r = create_courier.post_create_user(payload)
        assert r.status_code == 403 and r.json()['success'] is False and r.json()['message'] == "Email, password and name are required fields"
