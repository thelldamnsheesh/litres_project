import allure
from selene import browser, be


class BookPage:
    with allure.step('Открываем страницу книги'):
        def open(self, book):
            browser.open(f'/{book.book_type}{book.book_url}')
            return self

    with allure.step('Добавляем книгу в корзину'):
        def add_book_to_cart(self):
            browser.driver.execute_script("window.scrollTo(0,200)")
            browser.element('[data-testid="book__addToCartButton--desktop"]').should(be.visible).click()
            browser.element('[data-testid="modal__close--button"]').click()
            return self

    with allure.step('Добавляем книгу в избранное'):
        def add_book_to_favorites(self):
            browser.element('.FunctionalBlock-module__button_adaptive_v4nIh').should(be.visible).click()
            return self


book_page = BookPage()
