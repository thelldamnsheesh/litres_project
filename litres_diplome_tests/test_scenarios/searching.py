from litres_diplome_tests.pages.main_page import main_page


class TestSearching:
    def search_book_by_title(self, book):
        main_page.open()
        main_page.search_book_by_title(book)
        main_page.check_searching_results(book)
        return self

    def searching_book_by_fullname(self, book):
        main_page.open()
        main_page.search_book_bu_fullname(book)
        main_page.check_searching_by_fullname_results(book)
        return self

    def clean_search_input_string(self, book):
        main_page.open()
        main_page.search_book_by_title(book)
        main_page.clean_searching_string()
        return self


test_searching = TestSearching()
