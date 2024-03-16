import os
import allure
from litres_diplome_tests.data.users import User
from litres_diplome_tests.test_scenarios.authorization import test_authorization


@allure.epic('Авторизация пользователя')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'registered user')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_registered_user():
    user = User(
        name=os.getenv('USER_NAME'),
        password=os.getenv("USER_PASSWORD"),
        email=os.getenv('USER_EMAIL')
    )
    test_authorization.authorization_registered_user(user)


@allure.epic('Авторизация пользователя')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'unregistered user')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_authorization_unregistered_user():
    user = User(
        name=os.getenv('UR_USER_NAME'),
        password=os.getenv('UR_USER_PASSWORD'),
        email=os.getenv('UR_USER_EMAIL')
    )

    test_authorization.authorization_unregistered_user(user)
