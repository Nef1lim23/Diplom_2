import allure
import pytest

from data import *
from methods.user_methods import UserMethods


class TestCouriersEndpoints:

    @allure.title('Проверка создания уникального пользователя')
    @allure.description('Создаем уникального user с Faker и удаляем его по токену после теста'
                                                            'В ответе проверяются код и тело')
    def test_create_new_user_success(self, create_and_delete_user):
        payload, response = create_and_delete_user
        deserialization = response.json()
        assert response.status_code == 200 and response.json().get('success') is True
        assert 'accessToken' in deserialization and deserialization['accessToken'] != ''
        assert 'refreshToken' in deserialization and deserialization['refreshToken'] != ''
        assert deserialization['user']['email'] == payload['email']
        assert deserialization['user']['name'] == payload['name']

    @allure.title('создание пользователя, который уже зарегистрирован')
    def test_create_already_exist_user(self, create_and_delete_user):
        create_courier = UserMethods()
        payload, _ = create_and_delete_user
        r = create_courier.post_create_couriers(payload)
        deserialization = r.json()
        assert r.status_code == 403
        assert deserialization['success'] is False and deserialization['message'] == 'User already exists'

    @allure.title('создание пользователя без обязательльного поля')
    @pytest.mark.parametrize('payload', InvalidDataForRegistration.payloads)
    def test_create_user_without_required_field(self, payload):
        create_courier = UserMethods()
        r = create_courier.post_create_couriers(payload)
        assert r.status_code == 403 and r.json()['success'] is False and r.json()['message'] == "Email, password and name are required fields"
