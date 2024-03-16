import allure
from litres_diplome_tests.data.books import book, book2
from litres_diplome_tests.test_scenarios.searching import test_searching


@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_search_book_by_title():
    test_searching.search_book_by_title(book2)


@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_searching_book_by_fullname():
    test_searching.searching_book_by_fullname(book2)


@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_search_audiobook_by_title():
    test_searching.search_book_by_title(book)


@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_searching_audiobook_by_fullname():
    test_searching.searching_book_by_fullname(book)


@allure.epic('Поисковая строка')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_clean_search_input_string():
    test_searching.clean_search_input_string(book2)
