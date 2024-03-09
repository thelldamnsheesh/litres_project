import os
from pages.authorization_form import authorization
from pages.main_page import main_page
from data.users import User


def test_autorization_registred_user():
    user = User(
        name=os.getenv('USER_NAME'),
        password=os.getenv("USER_PASSWORD"),
        email=os.getenv('USER_EMAIL')
    )

    main_page.open()
    authorization.authorization_registred_user(user)
    authorization.check_user_info(user)


def test_autorization_unregistred_user():
    user = User(
        name=os.getenv('UR_USER_NAME'),
        password=os.getenv('UR_USER_PASSWORD'),
        email=os.getenv('UR_USER_EMAIL')
    )
    main_page.open()
    authorization.authorization_registred_user(user)
    authorization.user_must_not_be_authorized()
