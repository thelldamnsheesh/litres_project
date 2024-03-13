import allure

from litres_diplome_tests.pages.main_page import main_page
from litres_diplome_tests.pages.favorites_page import favorites_page
from litres_diplome_tests.pages.book_page import book_page
from litres_diplome_tests.data.books import book, book2


@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer','web')
def test_add_book_from_main():

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Ищем книгу по названию'):
        main_page.search_book_by_title(book2)

    with allure.step('Проверяем выполнение поискового запроса'):
        main_page.check_searching_results(book2)

    with allure.step('Добавляем книгу в избранные'):
        main_page.add_to_favorites_from_main()

    with allure.step('Проверяем наличие книги в избранном'):
        favorites_page.check_book_in_favorites(book2)

@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer','web')
def test_add_book_from_book_page():

    with allure.step('Открываем страницу книги'):
        book_page.open(book2)

    with allure.step('Добавляем книгу в избранные'):
        book_page.add_book_to_favorites()

    with allure.step('Проверяем наличие книги в избранном'):
        favorites_page.check_book_in_favorites(book2)

@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer','web')
def test_add_audiobook_from_main():

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Ищем аудиокнигу по названию'):
        main_page.search_book_by_title(book)

    with allure.step('Проверяем выполнение поискового запроса'):
        main_page.check_searching_results(book)

    with allure.step('Добавляем аудиокнигу в избранные'):
        main_page.add_to_favorites_from_main()

    with allure.step('Проверяем наличие книги в избранном'):
        favorites_page.check_book_in_favorites(book)


@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer','web')
def test_add_audiobook_from_audiobook_page():

    with allure.step('Открываем страницу аудиокниги'):
        book_page.open(book)

    with allure.step('Добавляем аудиокнигу в избранные'):
        book_page.add_book_to_favorites()

    with allure.step('Проверяем наличие аудиокниги в избранном'):
        favorites_page.check_book_in_favorites(book)