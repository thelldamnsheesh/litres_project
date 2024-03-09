from selene import browser, be, command


class BookPage:
    def open(self, book):
        browser.open(f'/{book.book_type}{book.book_url}')
        return self

    def add_book_to_cart(self):
        if browser.element('.CookieAcceptPopup-module__container_UndPF'):
            browser.element('CookieAcceptPopup-module__button_1G7Rp').perform(command.js.click)
        else:
            browser.execute_script("window.scrollTo(0,100)")
            browser.execute_script("window.scrollTo(0,100)")
            browser.element('[data-testid="book__addToCartButton--desktop"]').should(be.visible).click()
            browser.element('[data-testid="modal__close--button"]').click()
        return self

    def add_book_to_favorites(self):
        browser.element('.FunctionalBlock-module__button_adaptive_v4nIh').should(be.visible).click()
        return self


book_page = BookPage()
