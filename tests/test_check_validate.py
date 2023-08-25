import pytest


@pytest.mark.parametrize('data,expected_result',
                         [(12, "Valid"), (55, "Not in range"), ('pp', 'Not a number')],
                         ids=['12 - Valid', '55 -Not in range', 'pp- Not a number'])
def test_square_validation(check_validate, data, expected_result):
    check_validate.check_correct_value(data, expected_result)
