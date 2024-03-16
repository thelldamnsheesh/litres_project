import allure
from litres_diplome_tests.data.books import book, book2
from litres_diplome_tests.test_scenarios.remove_from_favorites import test_remove_from_favorites


@allure.epic('Удаление из избранного')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'book')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_remove_book_from_favorites():
    test_remove_from_favorites.remove_book_from_favorites(book2)


@allure.epic('Удаление из избранного')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'audiobook')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_remove_audiobook_from_favorites():
    test_remove_from_favorites.remove_book_from_favorites(book)
