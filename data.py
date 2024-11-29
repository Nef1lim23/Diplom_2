class URLs:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    POST_CREATE_USER = f'{BASE_URL}api/auth/register'
    LOGIN_COURIER_URL = f'{BASE_URL}api/auth/login'
    DELETE_COURIER_URL = f'{BASE_URL}api/auth/user/'    # возможно тут вместо юзера идет ИД



class Errors:
    error_login_400_no_login_or_pass = "Недостаточно данных для входа"
    error_login_404_no_such_user = "Учетная запись не найдена"
    error_create_400_no_data = "Недостаточно данных для создания учетной записи"
    error_create_409_already_exist = "Этот логин уже используется."
    error_delete_400_no_data = "Недостаточно данных для удаления курьера"
    error_delete_404_no_such_id = "Курьера с таким id нет."
    error_count_orders_no_data = "Недостаточно данных для поиска"
    error_count_orders_no_such_user = "Курьер не найден"
    error_track_order_no_data = "Недостаточно данных для поиска"
    error_track_order_no_such_order = "Заказ не найден"
    error_accept_order_no_order_number = "Недостаточно данных для поиска"
    error_accept_order_no_such_courier = "Курьера с таким id не существует"
    error_accept_order_no_data = "Недостаточно данных для поиска"


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

