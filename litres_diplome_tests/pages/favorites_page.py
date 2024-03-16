import allure
from selene import browser, have, be


class FavoritesPage:
    with allure.step('Проверяем наличие книги в избранном'):
        def check_book_in_favorites(self, book):
            browser.open('/my-books/liked/')
            browser.element('[data-testid="art__title"]').should(have.text(book.title))
            browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
            browser.element('.ArtPriceFooter-module__ArtPriceFooterPrices__final_2FPWa').should(have.text(book.price))
            if book.book_type == 'book':
                return self
            if book.book_type == 'audiobook':
                browser.element('.ArtInfo-modules__reader_4aV4e').should(have.text(f'Читает {book.reader}'))
                return self

    with allure.step('Удаляем книгу из избранного'):
        def remove_book_from_favorites(self):
            browser.open('/my-books/liked/')
            browser.element('div.ArtV2Default-module__like_button_1VLId > div').should(be.visible).click()
            browser.element('[data-testid="popover__content"]').should(have.text('Убрать из отложенного')).click()
            browser.driver.refresh()
            return self

    with allure.step('Проверяем, что в избранном пусто'):
        def check_empty_favorites(self):
            browser.element('.EmptyState-module__empty__content_2lpJ-').should(have.text('Здесь будет все, что вы '
                                                                                         'отложите на потом'))
            return self

    with allure.step('Добавляем книгу в корзину'):
        def add_book_to_cart(self):
            browser.open('/my-books/liked/')
            browser.element('div.ArtV2Default-module__like_button_1VLId > div').should(be.visible).click()
            browser.element('//*[@id=":r4:"]/div/div/div[2]').should(be.visible).click()
            return self


favorites_page = FavoritesPage()
