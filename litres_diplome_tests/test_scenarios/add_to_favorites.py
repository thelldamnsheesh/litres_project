from litres_diplome_tests.pages.book_page import book_page
from litres_diplome_tests.pages.favorites_page import favorites_page
from litres_diplome_tests.pages.main_page import main_page


class TestAddToFavorites:

    def add_book_to_favorites_from_main(self, book):
        main_page.open()
        main_page.search_book_by_title(book)
        main_page.check_searching_results(book)
        main_page.add_to_favorites_from_main()
        favorites_page.check_book_in_favorites(book)
        return self

    def add_book_to_favorites_from_book_page(self, book):
        book_page.open(book)
        book_page.add_book_to_favorites()
        favorites_page.check_book_in_favorites(book)
        return self

    def redirect_to_main(self, book):
        book_page.open(book)
        main_page.redirect_to_book_page()
        return self


test_add_to_favorites = TestAddToFavorites()
