import os
import allure
from jsonschema import validate
from litres_diplome_tests.utils.api_attach import request
from litres_diplome_tests.utils.load_schema import load_schema
from tests.api.conftest import SCHEMA_DIR, base_url, headers


@allure.epic('API тесты. Авторизация')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'positive')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_registered_user_authorization_api():
    schema = os.path.join(SCHEMA_DIR, "successful_authorization.json")
    api = '/auth/login'
    url = f'{base_url}{api}'
    email = os.getenv('USER_EMAIL')
    password = os.getenv('USER_PASSWORD')
    response = request(url, method='POST', headers=headers, json={"login": email, "password": password})
    assert response.status_code == 200
    validate(response.json(), load_schema(schema))
    assert response.json()['error'] is None


@allure.epic('API тесты. Авторизация')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'negative')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_invalid_password_user_authorization_api():
    schema = os.path.join(SCHEMA_DIR, "unsuccessful_authorization.json")
    api = '/auth/login'
    url = f'{base_url}{api}'
    invalid_email = os.getenv('USER_EMAIL')
    invalid_password = os.getenv('UR_USER_PASSWORD')
    response = request(url, method='POST', headers=headers, json={"login": invalid_email, "password": invalid_password})
    assert response.status_code == 401
    validate(response.json(), load_schema(schema))
    assert response.json()['error']['type'] == "Unauthorized"
    assert response.json()['error']['title'] == "Incorrect user data"
