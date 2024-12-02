import allure
from helpers import get_login_payload
from methods.user_methods import UserMethods

user_methods = UserMethods()


class TestUpdateUser:

    @allure.title('Обноление данных авторизованного пользователя')
    def test_update_auth_user(self, create_and_delete_user):
        payload = create_and_delete_user['payload']
        login_payload = get_login_payload(payload)
        login_response = user_methods.post_login_user(login_payload)
        assert login_response.status_code == 200 and login_response.json()["success"] is True
