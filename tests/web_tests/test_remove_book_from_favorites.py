from pages.favorites_page import favorites_page
from pages.main_page import main_page
from data.books import book


def test_remove_book_from_favorites():
    main_page.open()
    main_page.search_book_by_title(book)
    main_page.add_to_favorites_from_main()
    favorites_page.check_book_in_favorites(book)
    favorites_page.remove_book_from_favorites()
    favorites_page.check_empty_favorites()

def test_remove_audiobook_from_favorites():
    main_page.open()
    main_page.search_book_by_title(book)
    main_page.add_to_favorites_from_main()
    favorites_page.check_book_in_favorites(book)
    favorites_page.remove_book_from_favorites()
    favorites_page.check_empty_favorites()