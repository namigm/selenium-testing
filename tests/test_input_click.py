import pytest


@pytest.mark.parametrize('data', ["Namik"])
def test_add_something(input_click, data):
    input_click.add_item_check(data)

@pytest.mark.parametrize('data', ["Togrul"])
def test_remove_something(input_click, data):
    input_click.remove_item_check(data)
