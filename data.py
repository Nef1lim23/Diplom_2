from helpers import generate_ingredients


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


DUP_USER_RESPONSE = {
    "success": False,
    "message": "User already exists"
}

LOGIN_ERROR_RESPONSE = {
    'success': False,
    'message': 'email or password are incorrect'
}

PATCH_DATA_ERROR = {
    'success': False,
    'message': 'You should be authorised'
}

VALID_INGREDIENTS_PAYLOAD = {
    'ingredients': generate_ingredients()
}

EMPTY_INGREDIENTS_PAYLOAD = {
    'ingredients': []
}

INVALID_INGREDIENTS_PAYLOAD = {
    "ingredients": ["invalid_id_0", "invalid_id_1"]
}
