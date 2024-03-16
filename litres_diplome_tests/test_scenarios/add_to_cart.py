from litres_diplome_tests.pages.book_page import book_page
from litres_diplome_tests.pages.cart_page import cart_page
from litres_diplome_tests.pages.favorites_page import favorites_page


class TestAddToCart:
    def add_book_to_cart_from_book_page(self, book):
        book_page.open(book)
        book_page.add_book_to_cart()
        cart_page.check_book_in_a_cart(book)
        return self

    def add_book_to_cart_from_favorites(self, book):
        book_page.open(book)
        book_page.add_book_to_favorites()
        favorites_page.check_book_in_favorites(book)
        favorites_page.add_book_to_cart()
        cart_page.check_book_in_a_cart(book)
        return self


test_add_to_cart = TestAddToCart()
