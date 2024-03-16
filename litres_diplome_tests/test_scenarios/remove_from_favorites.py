from litres_diplome_tests.pages.book_page import book_page
from litres_diplome_tests.pages.favorites_page import favorites_page


class TestRemoveFromFavorites:
    def remove_book_from_favorites(self, book):
        book_page.open(book)
        book_page.add_book_to_favorites()
        favorites_page.check_book_in_favorites(book)
        favorites_page.remove_book_from_favorites()
        favorites_page.check_empty_favorites()


test_remove_from_favorites = TestRemoveFromFavorites()
