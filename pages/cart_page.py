from selene import browser, have, be



class CertPage:
    def check_book_in_a_cart(self, book):
        # Проверк книги в корзине
        browser.open('/my-books/cart/')
        browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(book.title))
        return self

    def remove_book_from_cart(self):
        # Удаление книги из корзины
        browser.element('[data-testid="cart__listDeleteButton--desktop"]').click()
        browser.element('.Modal-module__controls_1qN-h > .Button-module__button_primary_2FaKg').should(
            be.visible).click()
        return self


cart_page = CertPage()
