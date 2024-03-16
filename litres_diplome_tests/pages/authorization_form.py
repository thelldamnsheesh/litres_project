import allure
from selene import browser, be, have


class Authorization:
    with allure.step('Открываем форму авторизации и вводим почту и пароль'):
        def authorization_registered_user(self, user):
            browser.element('[href="/pages/login/"]').should(be.visible).click()
            browser.element('[name="email"]').should(be.visible).type(user.email)
            browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
            browser.element('[name="pwd"]').should(be.visible).type(user.password)
            browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
            return self

    with allure.step('Проверяем имя пользователя в личном кабинете'):
        def check_user_info(self, user):
            browser.element('[data-testid="header__profile-button"]').should(be.visible).click()
            browser.open("/pages/personal_cabinet_about_me/")
            browser.element('.user_header__name').should(have.text(user.name))
            return self

    with allure.step('Проверяем наличие заглушки'):
        def user_must_not_be_authorized(self):
            browser.element('.ControlInput-module__input__error_2jXOB').should(have.text('Неверное сочетание логина и '
                                                                                         'пароля'))
            return self


authorization = Authorization()
