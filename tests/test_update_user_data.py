import allure
from data import PATCH_DATA_ERROR
from methods.user_methods import UserMethods

user_methods = UserMethods()


class TestUpdateUser:

    @allure.title('Обновление данных авторизованного пользователя')
    def test_update_auth_user(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        update_response = user_methods.patch_data_user(access_token)
        assert update_response.status_code == 200 and update_response.json()['success'] is True

    @allure.title('Обновление данных  не авторизованного пользователя')
    def test_update_auth_user(self, create_and_delete_user):
        update_response = user_methods.patch_data_user('')
        assert update_response.status_code == 401 and update_response.json() == PATCH_DATA_ERROR
