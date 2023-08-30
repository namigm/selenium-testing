import pytest
from env_setup import *

def test_successful_login(index_page):
    index_page.login(WAPP_USER_NAME, WAPP_PASSWORD)
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

# Sozdat Json file, kuda napishesh odin obyekt, v etom obyekte budet para kluc znacenie. Eti znaceniya doljni parol user.
# Potom nado sdelat deserializaciya dannix, i pomestit ix v pyton, potom ispolzovat sdel eti znaceniya

