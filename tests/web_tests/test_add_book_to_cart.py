from qa_guru_diplome_tests.pages.cart_page import cart_page
from qa_guru_diplome_tests.pages.book_page import book_page
from qa_guru_diplome_tests.pages.favorites_page import favorites_page
from qa_guru_diplome_tests.data.books import book, book2
import allure


@allure.epic('Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_to_cart_from_book_page():

    with allure.step('Открываем страницу книги'):
        book_page.open(book)

    with allure.step('Добавляем книгу в корзину'):
        book_page.add_book_to_cart()

    with allure.step('Проверяем наличие книги в корзине'):
        cart_page.check_book_in_a_cart(book)


@allure.epic('Добавление в корзину')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('web')
def test_add_book_to_cart_from_favorites():

    with allure.step('Открываем страницу книги'):
        book_page.open(book2)

    with allure.step('Добавляем книгу в избранное'):
        book_page.add_book_to_favorites()

    with allure.step('Проверяем наличие книги в избранном'):
        favorites_page.check_book_in_favorites(book2)

    with allure.step('Добавляем книгу в корзину'):
        favorites_page.add_book_to_cart()

    with allure.step('Проверяем наличие книги в корзине'):
        cart_page.check_book_in_a_cart(book2)
