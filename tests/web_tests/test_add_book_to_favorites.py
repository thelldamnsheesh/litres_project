from pages.main_page import main_page
from pages.favorites_page import favorites_page
from pages.book_page import book_page
from data.books import book, book2


def test_add_book_from_main():
    main_page.open()
    main_page.search_book_by_title(book2)
    main_page.add_to_favorites_from_main()
    favorites_page.check_book_in_favorites(book2)

def test_add_book_from_book_page():
    book_page.add_book_to_favorites(book2)
    favorites_page.check_book_in_favorites(book2)

def test_add_audiobook_from_main():
    main_page.open()
    main_page.search_book_by_title(book)
    main_page.add_to_favorites_from_main()
    favorites_page.check_book_in_favorites(book)

def test_add_audiobook_from_book_page():
    book_page.add_book_to_favorites(book)
    favorites_page.check_book_in_favorites(book)