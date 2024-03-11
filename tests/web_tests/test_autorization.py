import os
from qa_guru_diplome_tests.pages.authorization_form import authorization
from qa_guru_diplome_tests.pages.main_page import main_page
from qa_guru_diplome_tests.data.users import User
import allure


@allure.epic('Авторизация пользователя')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'registred user')
@allure.severity('normal')
@allure.label('layer','web')
def test_autorization_registred_user():
    user = User(
        name=os.getenv('USER_NAME'),
        password=os.getenv("USER_PASSWORD"),
        email=os.getenv('USER_EMAIL')
    )

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Открываем форму авторизации и вводим почту и пароль'):
        authorization.authorization_registred_user(user)

    with allure.step('Проверяем имя пользователя в личном кабинете'):
        authorization.check_user_info(user)


@allure.epic('Авторизация пользователя')
@allure.label("owner", "thelldamnsiiuu")
@allure.tag('regress', 'web', 'unregistred user')
@allure.severity('normal')
@allure.label('layer','web')
def test_autorization_unregistred_user():
    user = User(
        name=os.getenv('UR_USER_NAME'),
        password=os.getenv('UR_USER_PASSWORD'),
        email=os.getenv('UR_USER_EMAIL')
    )

    with allure.step('Открываем главную страницу'):
        main_page.open()

    with allure.step('Открываем форму авторизации и вводим почту и пароль'):
        authorization.authorization_registred_user(user)

    with allure.step('Проверяем наличие заглушки'):
        authorization.user_must_not_be_authorized()
