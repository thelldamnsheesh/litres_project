from selene import browser, be, have


class Authorization:


def test_search_book():
    #Авторизация
    browser.open('https://www.litres.ru/')
    browser.element('[href="/pages/login/"]').should(be.visible).click()
    browser.element('[name="email"]').should(be.visible).type('evgeny.globe@yandex.ru')
    browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
    browser.element('[name="pwd"]').should(be.visible).type('ParolLitres')
    browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()




    #Проверка авторизации
    browser.element('[data-testid="header__profile-button"]').should(be.visible).click()
    browser.open("pages/personal_cabinet_about_me/")
    browser.element('span[class="user_header__name"]').should(have.text('evgeny.globe'))

    # Добавление книги в корзину



    # Проверк книги в корзине
    browser.open('https://www.litres.ru/my-books/cart/')
    browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text('Златан Ибрагимович. Только '
                                                                                   'бог может судить меня'))


    #Удаление книги из корзины
    browser.element('[data-testid="cart__listDeleteButton--desktop"]').click()
    browser.element('.Modal-module__controls_1qN-h > .Button-module__button_primary_2FaKg').should(be.visible).click()



    #Поиск книги по названию
    (browser.element('[data-testid="header__search-button--desktop"]').should(be.visible)
     .type(" Златан Ибрагимович. Только бог может судить меня").press_enter())

    browser.element('[data-testid="search-title__wrapper"]').should(have.text('Результаты поиска «Златан Ибрагимович. '
                                                                              'Только бог может судить меня»'))

    #Добавление в избранные
    browser.element('.ArtV2Default-module__like_button_1VLId').should(be.visible).click()

    #удаление из избранного
    browser.open('https://www.litres.ru/my-books/liked/')
    browser.element('div.ArtV2Default-module__like_button_1VLId > div').should(be.visible).click()
    browser.element('//*[@id=":r4:"]/div/div/div[3]').should(be.visible).click()

    #Проверка пустого избранного
    browser.element('.EmptyState-module__empty__content_2lpJ-').should(have.text('Здесь будет все, что вы '
                                                                                     'отложите на потом'))


    #Проверка истории поиска
    (browser.element('[data-testid="header__search-button--desktop"]').should(be.visible)
     .type(" Мастер и Маргарита"))
    browser.element('.SearchForm-module__clear_33FdF').click()
















