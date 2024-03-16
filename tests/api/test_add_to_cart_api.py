import os.path
import allure
from jsonschema import validate
from litres_diplome_tests.utils.load_schema import load_schema
from litres_diplome_tests.utils.api_attach import request
from litres_diplome_tests.data.books import book, book2
from tests.api.conftest import SCHEMA_DIR, base_url, headers


@allure.epic('API тесты. Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_add_audiobook_to_cart_put_api():

    schema = os.path.join(SCHEMA_DIR, "add_book_to_cart.json")
    api = '/cart/arts/add'
    url = f'{base_url}{api}'
    payload = {"art_ids": book.art_type}

    response = request(url, method='PUT', headers=headers, json=payload)
    assert response.status_code == 200
    validate(response.json(), load_schema(schema))

    assert response.json()['payload']['data']['added_art_ids'] == book.art_type
    assert response.json()['payload']['data']['failed_art_ids'] == []


@allure.epic('API тесты. Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_add_book_to_cart_put_api():
    schema = os.path.join(SCHEMA_DIR, "add_book_to_cart.json")
    api = '/cart/arts/add'
    url = f'{base_url}{api}'
    payload = {"art_ids": book2.art_type}

    response = request(url, method='PUT', headers=headers, json=payload)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))
    assert response.json()['payload']['data']['added_art_ids'] == book2.art_type
    assert response.json()['payload']['data']['failed_art_ids'] == []
