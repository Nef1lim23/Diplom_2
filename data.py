class URLs:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    POST_CREATE_USER = f'{BASE_URL}auth/register'
    LOGIN_USER_URL = f'{BASE_URL}auth/login'
    DELETE_COURIER_URL = f'{BASE_URL}auth/user'
    GET_INFO_FOR_USER = f'{BASE_URL}auth/user'


class InvalidDataForRegistration:
    payloads = [
        {
            'name': 'Rick',
            'email': 'korneev_14123@gmail.ru',
            'password': ''

        },
        {
            'name': 'Rick12',
            'email': '',
            'password': '123123'

        },
        {
            'name': '',
            'email': 'korneev_1456546@gmail.ru',
            'password': '123123'

        }
    ]

class UserData:
    email = "testdiplom_1@mail.ru"
    password = "test123_1"
    name = "test_dip"


DUP_USER_RESPONSE = {
        "success": False,
        "message": "User already exists"
    }

LOGIN_ERROR_RESPONSE = {
        'success': False,
        'message': 'email or password are incorrect'
    }
