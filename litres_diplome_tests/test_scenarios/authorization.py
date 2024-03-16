from litres_diplome_tests.pages.authorization_form import authorization
from litres_diplome_tests.pages.main_page import main_page


class TestAuthorization:
    def authorization_registered_user(self, user):
        main_page.open()
        authorization.authorization_registered_user(user)
        authorization.check_user_info(user)
        return self

    def authorization_unregistered_user(self, user):
        main_page.open()
        authorization.authorization_registered_user(user)
        authorization.user_must_not_be_authorized()
        return self


test_authorization = TestAuthorization()
