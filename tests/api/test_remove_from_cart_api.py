import allure
from litres_diplome_tests.data.books import book2, book
from litres_diplome_tests.utils.api_attach import request

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}


@allure.epic('API тесты. Удаление из корзины')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'book')
@allure.severity('normal')
@allure.label('layer','api')
def test_remove_book_from_cart():
    api = '/cart/arts/remove'
    url = f'{base_url}{api}'
    payload = {"art_ids": book2.art_type}

    response = request(url, method='PUT', headers=headers, json=payload)

    assert response.status_code == 204
    assert response.text == ''


@allure.epic('API тесты. Удаление из корзины')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'api', 'audiobook')
@allure.severity('normal')
@allure.label('layer','api')
def test_remove_audiobook_from_cart():
    api = '/cart/arts/remove'
    url = f'{base_url}{api}'
    payload = {"art_ids": book.art_type}

    response = request(url, method='PUT', headers=headers, json=payload)

    assert response.status_code == 204
    assert response.text == ''
