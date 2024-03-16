import allure
from litres_diplome_tests.data.books import book, book2
from litres_diplome_tests.test_scenarios.add_to_cart import test_add_to_cart


@allure.epic('Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_to_cart_from_book_page():
    test_add_to_cart.add_book_to_cart_from_book_page(book)


@allure.epic('Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_to_cart_from_favorites():
    test_add_to_cart.add_book_to_cart_from_favorites(book2)
