import os
from urllib.parse import quote
import allure
from utils.load_schema import load_schema
import schemas
from data.books import book, book2
from utils.api_attach import api_get
from jsonschema import validate

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}
SCHEMA_INIT = os.path.abspath(schemas.__file__)
SCHEMA_DIR = os.path.dirname(SCHEMA_INIT)


@allure.epic('API тесты. Поиск книги/аудиокниги')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'audiobook')
@allure.severity('normal')
@allure.label('api')
def test_get_search_audiobook_by_title():
    schema = os.path.join(SCHEMA_DIR, "searching_book.json")
    query = quote(book.title)
    api = '/search'
    url = f'{base_url}{api}?limit=12&q={query}%&types={book.query_type}'
    response = api_get(url, headers=headers)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))


@allure.epic('API тесты. Поиск книги/аудиокниги')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book')
@allure.severity('normal')
@allure.label('api')
def test_get_search_book_by_title():
    schema = os.path.join(SCHEMA_DIR, "searching_book.json")
    query = quote(book2.title)
    api = '/search'
    url = f'{base_url}{api}?limit=12&q={query}%&types={book2.query_type}'
    response = api_get(url, headers=headers)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))
    a = response.json()


@allure.epic('API тесты. Поиск книги/аудиокниги')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book', 'negative')
@allure.severity('normal')
@allure.label('api')
def test_get_search_book_by_title_negative_api():
    schema = os.path.join(SCHEMA_DIR, "unsuccessful_searching_book.json")
    query = 'dfvbaab SEFdfS '
    api = '/search'
    url = f'{base_url}{api}?limit=12&q={query}%&types={book2.query_type}'
    response = api_get(url, headers=headers)

    assert response.status_code == 200
    validate(response.json(), load_schema(schema))
