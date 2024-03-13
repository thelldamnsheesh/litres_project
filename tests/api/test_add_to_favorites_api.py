import allure
from litres_diplome_tests.data.books import book2, book
from litres_diplome_tests.utils.api_attach import request

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}


@allure.epic('API тесты. Добавление в избранные')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book')
@allure.severity('normal')
@allure.label('layer','api')
def test_add_book_to_favorite_api():
    api = '/wishlist/arts/'
    art_type = book2.art_type[0]
    url = f'{base_url}{api}{art_type}'
    response = request(url, method='PUT')

    assert response.status_code == 204
    assert response.text == ''


@allure.epic('API тесты. Добавление в избранные')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'audiobook')
@allure.severity('normal')
@allure.label('layer','api')
def test_add_book_to_favorite_api():
    api = '/wishlist/arts/'
    art_type = book.art_type[0]
    url = f'{base_url}{api}{art_type}'
    response = request(url, method='PUT')

    assert response.status_code == 204
    assert response.text == ''
