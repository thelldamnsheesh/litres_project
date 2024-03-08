from selene import browser, be, have
from data.books import book


class BookPage:
    def test_add_book_in_a_cart(self, book):
        browser.open(book.book_url)
        browser.execute_script("window.scrollTo(0,100)")
        browser.element('[data-testid="book__addToCartButton--desktop"]').should(be.visible).click()
        browser.element('[data-testid="modal__close--button"]').click()

    def test_check_book_in_a_cart(self, book):
        browser.open('/my-books/cart/')
        browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(book.title))

book_page = BookPage()