import allure
from litres_diplome_tests.data.books import book, book2
from litres_diplome_tests.test_scenarios.remove_from_cart import tests_remove_from_cart


@allure.epic('Удаление из корзины')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_remove_book_from_cart():
    tests_remove_from_cart.remove_book_from_cart(book2)


@allure.epic('Удаление из корзины')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_remove_book_from_cart_and_add_to_favorites():
    tests_remove_from_cart.remove_book_from_cart_and_add_to_favorites(book)
