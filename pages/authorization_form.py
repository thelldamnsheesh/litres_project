from selene import browser, be, have


class Authorization:
    #Авторизация
    def authorization_registred_user(self, user):
        browser.element('[href="/pages/login/"]').should(be.visible).click()
        browser.element('[name="email"]').should(be.visible).type(user.email)
        browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
        browser.element('[name="pwd"]').should(be.visible).type(user.password)
        browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()

    def check_user_info(self, user):
        # Проверка авторизации
        browser.element('[data-testid="header__profile-button"]').should(be.visible).click()
        browser.open("pages/personal_cabinet_about_me/")
        browser.element('span[class="user_header__name"]').should(have.text(user.name))

    def user_must_not_be_authorized(self):
        browser.element('.ControlInput-module__input__error_2jXOB').should(have.text('Неверное сочетание логина и '
                                                                                     'пароля'))

authorization = Authorization()