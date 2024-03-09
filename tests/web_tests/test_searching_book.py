from pages.main_page import main_page
from data.books import book, book2


def test_search_book_by_title():
    main_page.open()
    main_page.search_book_by_title(book2)
    main_page.check_searching_results(book2)

def test_searching_book_by_fullname():
    main_page.open()
    main_page.search_book_bu_fullname(book2)
    main_page.check_searching_by_fullname_results(book2)

def test_search_audiobook_by_title():
    main_page.open()
    main_page.search_book_by_title(book)
    main_page.check_searching_results(book)

def test_searching_audiobook_by_fullname():
    main_page.open()
    main_page.search_book_bu_fullname(book)
    main_page.check_searching_by_fullname_results(book)

def test_clean_search_input_string():
    main_page.open()
    main_page.clean_searching_string()
