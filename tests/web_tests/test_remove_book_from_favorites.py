from pages.favorites_page import favorites_page
from pages.book_page import book_page
from data.books import book, book2
import allure


@allure.epic('Удаление из избранного')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('web')
def test_remove_book_from_favorites():

    with allure.step('Открываем страницу книги'):
        book_page.open(book2)

    with allure.step('Добавляем книгу в избранные'):
        book_page.add_book_to_favorites()

    with allure.step('Проверяем наличие книги в избранном'):
        favorites_page.check_book_in_favorites(book2)

    with allure.step('Удаляем книгу из избранного'):
        favorites_page.remove_book_from_favorites()

    with allure.step('Проверяем, что в избранном пусто'):
        favorites_page.check_empty_favorites()

@allure.epic('Удаление из избранного')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('web')
def test_remove_audiobook_from_favorites():

    with allure.step('Открываем страницу аудиокниги'):
        book_page.open(book)

    with allure.step('Добавляем аудиокнигу в избранные'):
        book_page.add_book_to_favorites()

    with allure.step('Проверяем наличие аудиокниги в избранном'):
        favorites_page.check_book_in_favorites(book)

    with allure.step('Удаляем аудиокнигу из избранного'):
        favorites_page.remove_book_from_favorites()

    with allure.step('Проверяем, что в избранном пусто'):
        favorites_page.check_empty_favorites()