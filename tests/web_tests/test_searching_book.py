from pages.main_page import main_page
from data.books import book, book2
import allure


@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('web')
def test_search_book_by_title():

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Ищем книгу по названию'):
        main_page.search_book_by_title(book2)

    with allure.step('Проверяем результат поиска'):
       main_page.check_searching_results(book2)

@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('web')
def test_searching_book_by_fullname():

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Ищем книгу по полному названию (Название и автор)'):
        main_page.search_book_bu_fullname(book2)

    with allure.step('Проверяем результат поиска'):
        main_page.check_searching_by_fullname_results(book2)

@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('web')
def test_search_audiobook_by_title():

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Ищем книгу по названию'):
        main_page.search_book_by_title(book)

    with allure.step('Проверяем результат поиска'):
        main_page.check_searching_results(book)

@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('web')
def test_searching_audiobook_by_fullname():

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Ищем книгу по полному названию (Название и автор)'):
        main_page.search_book_bu_fullname(book)

    with allure.step('Проверяем результат поиска'):
        main_page.check_searching_by_fullname_results(book)

@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('web')
def test_clean_search_input_string():

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Вводим название книги в поисковое поле'):
        main_page.search_book_by_title(book2)

    with allure.step('Чистим поисковую строку по нажатию на кнопку "х"'):
        main_page.clean_searching_string()
