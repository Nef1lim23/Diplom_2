import requests
import random
import string
from faker import Faker
import data
import requests
from data import URLs


def create_random_creds():
    fake = Faker()
    email = fake.free_email()
    name = email.split('@')[0]
    password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }
    return payload