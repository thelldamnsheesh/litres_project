import logging
import os
from urllib.parse import quote

import allure

from utils.api_attach import api_get, api_post, api_put
from data.books import book


#base_url = 'https://api.litres.ru/foundation/api'
base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}



def test_add_to_cart_put_api():
    #url = 'https://api.litres.ru/foundation/api/cart/arts/add'
    api = '/cart/arts/add'
    url = f'{base_url}{api}'
    payload = {"art_ids": [69956326]}

    response = api_put(url, headers=headers, json=payload)

    assert response.status_code == 200


def test_get_search_book_by_title():
    query = quote(book.title)
    api = '/search'
    url = f'{base_url}{api}?limit=12&q={query}%&types={book.book_type}'
    response = api_get(url, headers=headers)

    assert response.status_code == 200


def test_api_authorization():
    api = '/auth/login'
    url = f'{base_url}{api}'
    email = os.getenv('USER_EMAIL')
    password = os.getenv('USER_PASSWORD')
    response = api_post(url, headers=headers, json={"login": email, "password": password})
    assert response.status_code == 200
