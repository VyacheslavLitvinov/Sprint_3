import random
import pytest


@pytest.fixture
def generate_valid_password():
    password = ''.join(
        [random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()-=+')) for x in
         range(6)])
    return password

@pytest.fixture
def generate_not_valid_password():
    password = ''.join(
        [random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%&*()-=+')) for x in
         range(5)])
    return password


@pytest.fixture
def generate_email():
    email = ''.join(
        [random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_-')) for x in range(15)])
    return 'Burger_' + email + '@burgers.souce'


