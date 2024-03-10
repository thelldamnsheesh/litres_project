from selene import be, browser, have


class MainPage:

    def open(self):
        browser.open("")
        return self

    def search_book_by_title(self, book):
        (browser.element('[data-testid="header__search-button--desktop"]').should(be.visible)
         .type(f' {book.title}').press_enter())
        return self

    def check_searching_results(self, book):
        browser.element('[data-testid="search-title__wrapper"]').should(
            have.text(f'Результаты поиска «{book.title}»'))
        browser.element('[data-testid="art__title"]').should(have.text(book.title))
        browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
        browser.element('.ArtPriceFooter-module__ArtPriceFooterPrices__final_2FPWa').should(have.text(book.price))
        if book.book_type == 'book':
            return self
        if book.book_type == 'audiobook':
            browser.element('.ArtInfo-modules__reader_4aV4e').should(have.text(f'Читает {book.reader}'))
            return self

    def add_to_favorites_from_main(self):
        browser.element('.ArtV2Default-module__like_button_1VLId').should(be.visible).click()
        return self

    def clean_searching_string(self):
        browser.element('.SearchForm-module__clear_33FdF').should(be.visible).click()
        return self

    def search_book_bu_fullname(self, book):
        (browser.element('[data-testid="header__search-button--desktop"]').should(be.visible)
         .type(f' {book.title} {book.author}').press_enter())
        return self

    def check_searching_by_fullname_results(self, book):
        browser.element('[data-testid="search-title__wrapper"]').should(
            have.text(f'Результаты поиска «{book.title} {book.author}»'))
        browser.element('[data-testid="art__title"]').should(have.text(book.title))
        browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
        browser.element('.ArtPriceFooter-module__ArtPriceFooterPrices__final_2FPWa').should(have.text(book.price))
        if book.book_type == 'book':
            return self
        if book.book_type == 'audiobook':
            browser.element('.ArtInfo-modules__reader_4aV4e').should(have.text(f'Читает {book.reader}'))
            return self

    def redirect_to_book_page(self):
        browser.element('[data-testid="art__title"]').click()
        return self


main_page = MainPage()
