from selene import be, browser, have

from data.books import book


class MainPage:
    def test_search_book_by_title(self, book):
        (browser.element('[data-testid="header__search-button--desktop"]').should(be.visible)
         .type(book.title).press_enter())

    def test_check_searching_results(self, book):
        browser.element('[data-testid="search-title__wrapper"]').should(
            have.text(f'Результаты поиска «{book.title}»'))
    def test_add_to_favorites_from_main(self):
        browser.element('.ArtV2Default-module__like_button_1VLId').should(be.visible).click()

    def test_clean_searching_string(self):
        browser.element('[data-testid="header__search-button--desktop"]').should(be.visible).type('1')
        browser.element('.SearchForm-module__clear_33FdF').should(be.visible).click()