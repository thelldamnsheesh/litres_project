import allure
from qa_guru_diplome_tests.data.books import book2, book
from qa_guru_diplome_tests.utils.api_attach import api_put

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}


@allure.epic('API тесты. Добавление в избранные')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book')
@allure.severity('normal')
@allure.label('api')
def test_add_book_to_favorite_api():
    api = '/wishlist/arts/'
    art_type = book2.art_type[0]
    url = f'{base_url}{api}{art_type}'
    response = api_put(url)

    assert response.status_code == 204
    assert response.text == ''


@allure.epic('API тесты. Добавление в избранные')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'audiobook')
@allure.severity('normal')
@allure.label('api')
def test_add_book_to_favorite_api():
    api = '/wishlist/arts/'
    art_type = book.art_type[0]
    url = f'{base_url}{api}{art_type}'
    response = api_put(url)

    assert response.status_code == 204
    assert response.text == ''
