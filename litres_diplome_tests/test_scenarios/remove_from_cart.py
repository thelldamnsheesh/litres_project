from litres_diplome_tests.pages.book_page import book_page
from litres_diplome_tests.pages.cart_page import cart_page
from litres_diplome_tests.pages.favorites_page import favorites_page


class TestRemoveFromCart:
    def remove_book_from_cart(self, book):
        book_page.open(book)
        book_page.add_book_to_cart()
        cart_page.check_book_in_a_cart(book)
        cart_page.remove_book_from_cart()
        cart_page.check_empty_cart()
        return self

    def remove_book_from_cart_and_add_to_favorites(self, book):
        book_page.open(book)
        book_page.add_book_to_cart()
        cart_page.check_book_in_a_cart(book)
        cart_page.remove_book_from_cart_and_add_to_favorites()
        cart_page.check_empty_cart()
        favorites_page.check_book_in_favorites(book)
        return self


tests_remove_from_cart = TestRemoveFromCart()
