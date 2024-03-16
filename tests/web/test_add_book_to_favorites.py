import allure
from litres_diplome_tests.data.books import book, book2
from litres_diplome_tests.test_scenarios.add_to_favorites import test_add_to_favorites


@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_from_main():
    test_add_to_favorites.add_book_to_favorites_from_main(book2)


@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_book_from_book_page():
    test_add_to_favorites.add_book_to_favorites_from_book_page(book2)


@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_audiobook_to_favorites_from_main():
    test_add_to_favorites.add_book_to_favorites_from_main(book)


@allure.epic('Добавление в избранное')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_add_audiobook_to_favorites_from_audiobook_page():
    test_add_to_favorites.add_book_to_favorites_from_book_page(book)


@allure.epic('Переход на главную страницу по нажатию на лого в шапке')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_redirect_to_main():
    test_add_to_favorites.redirect_to_main(book)
