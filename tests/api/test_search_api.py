import os
from urllib.parse import quote
import allure
from litres_diplome_tests.utils.load_schema import load_schema
from litres_diplome_tests import schemas
from litres_diplome_tests.data.books import book, book2
from litres_diplome_tests.utils.api_attach import request
from jsonschema import validate

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}
SCHEMA_INIT = os.path.abspath(schemas.__file__)
SCHEMA_DIR = os.path.dirname(SCHEMA_INIT)


@allure.epic('API тесты. Поиск книги/аудиокниги')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'audiobook')
@allure.severity('normal')
@allure.label('layer','api')
def test_get_search_audiobook_by_title():
    schema = os.path.join(SCHEMA_DIR, "searching_book.json")
    query = quote(book.title)
    params = {
        "limit": 12,
        "q": f"{query}%",
        "types": book.query_type
    }
    api = '/search'
    url = f'{base_url}{api}?'
    response = request(url, method='GET', headers=headers, params=params)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))


@allure.epic('API тесты. Поиск книги/аудиокниги')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book')
@allure.severity('normal')
@allure.label('layer','api')
def test_get_search_book_by_title():
    schema = os.path.join(SCHEMA_DIR, "searching_book.json")
    query = quote(book2.title)
    params = {
        "limit": 12,
        "q": f"{query}%",
        "types": book.query_type
    }
    api = '/search'
    url = f'{base_url}{api}?'
    response = request(url, method='GET', headers=headers, params=params)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))


@allure.epic('API тесты. Поиск книги/аудиокниги')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book', 'negative')
@allure.severity('normal')
@allure.label('layer','api')
def test_get_search_book_by_title_negative_api():
    schema = os.path.join(SCHEMA_DIR, "unsuccessful_searching_book.json")
    query = 'dfvbaab SEFdfS '
    api = '/search'
    params = {
        "limit": 12,
        "q": f"{query}%",
        "types": book.query_type
    }
    url = f'{base_url}{api}?'
    response = request(url, method='GET', headers=headers, params=params)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))
