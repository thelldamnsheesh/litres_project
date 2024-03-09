from pages.cart_page import cart_page
from pages.book_page import book_page
from data.books import book

def test_remove_book_from_cart():
    book_page.add_book_to_cart(book)
    cart_page.check_book_in_a_cart(book)
    cart_page.remove_book_from_cart()
    cart_page.check_book_in_a_cart()
