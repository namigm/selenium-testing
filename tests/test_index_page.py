import pytest

def test_successful_login(index_page):
    index_page.login(user_name="correct_username", password="correct_password")
    index_page.is_logged_in()


# sozdat dva testa
# 1. Ne uspeshiy login. koqda parol ne pravilniy
# ne uspeshiy login s ispolzovaniem pustoqo login name


@pytest.mark.parametrize('user_name,password,expected_result',
                         [('correct_username', 'correct_passward', 'Password or userme is incorrect'),
                          ('', 'correct_password', 'Username field cannot be empty')],
                         ids=['Not correct credentials', 'Empty password'])
def test_unsuccessful_login(index_page, user_name, password, expected_result):
    index_page.login(user_name, password)
    index_page.check_error_message(expected_result)






