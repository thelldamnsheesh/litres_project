from selene import browser, have, be



class CertPage:
    def check_book_in_a_cart(self, book):
        # Проверк книги в корзине
        browser.open('/my-books/cart/')
        browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(book.title))
        browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book.author))
        browser.element('[data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book.price))
        return self

    def remove_book_from_cart(self):
        # Удаление книги из корзины
        browser.element('[data-testid="cart__listDeleteButton--desktop"]').click()
        browser.element('.Modal-module__controls_1qN-h > .Button-module__button_primary_2FaKg').should(
            be.visible).click()
        return self

    def remove_book_from_cart_and_add_to_favorites(self):
        browser.element('[data-testid="cart__listDeleteButton--desktop"]').should(be.visible).click()
        browser.element('.Modal-module__controls_1qN-h > .Button-module__button_secondary_2G8Ew').should(
            be.visible).click()
        return self


    def check_empty_cart(self):
        browser.element('.EmptyState-module__empty__title_22qdT').should(have.text('Корзина пуста'))
        return self




cart_page = CertPage()
