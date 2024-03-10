import os
import allure
from jsonschema import validate
from qa_guru_diplome_tests import schemas
from qa_guru_diplome_tests.utils.api_attach import api_post
from qa_guru_diplome_tests.utils.load_schema import load_schema

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}
SCHEMA_INIT = os.path.abspath(schemas.__file__)
SCHEMA_DIR = os.path.dirname(SCHEMA_INIT)


@allure.epic('API тесты. Авторизация')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'positive')
@allure.severity('normal')
@allure.label('api')
def test_registred_user_authorization_api():
    schema = os.path.join(SCHEMA_DIR, "successful_authorization.json")
    api = '/auth/login'
    url = f'{base_url}{api}'
    email = os.getenv('USER_EMAIL')
    password = os.getenv('USER_PASSWORD')
    response = api_post(url, headers=headers, json={"login": email, "password": password})
    assert response.status_code == 200
    validate(response.json(), load_schema(schema))
    assert response.json()['error'] is None


@allure.epic('API тесты. Авторизация')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'negative')
@allure.severity('normal')
@allure.label('api')
def test_invalid_password_user_authorization_api():
    schema = os.path.join(SCHEMA_DIR, "unsuccessful_authorization.json")
    api = '/auth/login'
    url = f'{base_url}{api}'
    invalid_email = os.getenv('USER_EMAIL')
    invalid_password = os.getenv('UR_USER_PASSWORD')
    response = api_post(url, headers=headers, json={"login": invalid_email, "password": invalid_password})
    assert response.status_code == 401
    print(response.json())
    validate(response.json(), load_schema(schema))
    assert response.json()['error']['type'] == "Unauthorized"
    assert response.json()['error']['title'] == "Incorrect user data"
