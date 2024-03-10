from qa_guru_diplome_tests.pages.cart_page import cart_page
from qa_guru_diplome_tests.pages.book_page import book_page
from qa_guru_diplome_tests.pages.favorites_page import favorites_page
from qa_guru_diplome_tests.data.books import book, book2
import allure


@allure.epic('Удаление из корзины')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('web')
def test_remove_book_from_cart():

    with allure.step('Открываем страницу книги'):
        book_page.open(book2)

    with allure.step('Добавляем книгу в корзину'):
        book_page.add_book_to_cart()

    with allure.step('Проверяем наличие книги в корзине'):
        cart_page.check_book_in_a_cart(book2)

    with allure.step('Удаляем книгу из корзины по нажатию кнопки'):
        cart_page.remove_book_from_cart()

    with allure.step('Проверяем что корзина пуста'):
        cart_page.check_empty_cart()


@allure.epic('Удаление из корзины')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('web')
def test_remove_book_from_cart_and_add_to_favorites():

    with allure.step('Открываем страницу книги'):
        book_page.open(book)

    with allure.step('Добавляем книгу в корзину'):
        book_page.add_book_to_cart()

    with allure.step('Проверяем наличие книги в корзине'):
        cart_page.check_book_in_a_cart(book)

    with allure.step('Удаляем книгу из корзины и добавляем в избранные по нажатию кнопки'):
        cart_page.remove_book_from_cart_and_add_to_favorites()

    with allure.step('Проверяем что корзина пуста'):
        cart_page.check_empty_cart()

    with allure.step('Проверяем наличие книги в избранном'):
        favorites_page.check_book_in_favorites(book)
