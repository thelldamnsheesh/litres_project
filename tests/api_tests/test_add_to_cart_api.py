import os.path
import allure
from jsonschema import validate
from qa_guru_diplome_tests import schemas
from qa_guru_diplome_tests.utils.load_schema import load_schema
from qa_guru_diplome_tests.utils.api_attach import api_put
from qa_guru_diplome_tests.data.books import book, book2

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}
SCHEMA_INIT = os.path.abspath(schemas.__file__)
SCHEMA_DIR = os.path.dirname(SCHEMA_INIT)


@allure.epic('API тесты. Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'audiobook')
@allure.severity('normal')
@allure.label('api')
def test_add_audiobook_to_cart_put_api():
    schema = os.path.join(SCHEMA_DIR, "add_book_to_cart.json")
    api = '/cart/arts/add'
    url = f'{base_url}{api}'
    payload = {"art_ids": book.art_type}

    response = api_put(url, headers=headers, json=payload)
    assert response.status_code == 200
    validate(response.json(), load_schema(schema))

    assert response.json()['payload']['data']['added_art_ids'] == book.art_type
    assert response.json()['payload']['data']['failed_art_ids'] == []


@allure.epic('API тесты. Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book')
@allure.severity('normal')
@allure.label('api')
def test_add_book_to_cart_put_api():
    schema = os.path.join(SCHEMA_DIR, "add_book_to_cart.json")
    api = '/cart/arts/add'
    url = f'{base_url}{api}'
    payload = {"art_ids": book2.art_type}

    response = api_put(url, headers=headers, json=payload)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))
    assert response.json()['payload']['data']['added_art_ids'] == book2.art_type
    assert response.json()['payload']['data']['failed_art_ids'] == []
