from pytest import mark




@mark.parametrize("first_number,second_number, result", ([1, 2, 3], [2, 3, 5]),ids=["first_scenarion","second_scenario"])
def test_sum(first_number, second_number, result):
    assert first_number + second_number == result



