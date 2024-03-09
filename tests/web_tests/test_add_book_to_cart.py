from selene import browser

from pages.cart_page import cart_page
from pages.main_page import main_page
from pages.book_page import book_page
from pages.favorites_page import favorites_page
from data.books import book
import allure

class Helper:
    def scroll(self):
        browser.execute_script("window.scrollTo(0,100)")
help = Helper()

@allure.epic('Добавление книги в корзину с главной страницы')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_to_cart_from_main_page():


    with allure.step('Открываем страницу книги'):
        book_page.open(book)

    with allure.step('Скролли вниз'):
        help.scroll()

    with allure.step('Добавляем книгу в корзину'):
        book_page.add_book_to_cart()

    with allure.step('Проверяем наличие книги в корзине'):
        cart_page.check_book_in_a_cart(book)


@allure.epic('Добавление книги в корзину из избранного')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_to_cart_from_favorites():

    with allure.step('Открываем страницу книги'):
        book_page.open(book)

    with allure.step('Добавляем книгу в избранное'):
        book_page.add_book_to_favorites()

    with allure.step('Проверяем наличие книги в избранном'):
        favorites_page.check_book_in_favorites(book)

    with allure.step('Добавляем книгу в корзину'):
        favorites_page.add_book_to_cart()

    with allure.step('Проверяем наличие книги в корзине'):
        cart_page.check_book_in_a_cart(book)


def test_test():
    book_page.open(book)
    help.scroll()
    book_page.add_book_to_cart()
    cart_page.check_book_in_a_cart(book)
