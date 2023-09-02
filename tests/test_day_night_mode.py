@pytest.mark.smoke
def test_night_mode(day_night):
    day_night.check_night_mode()


def test_day_mode(day_night):
    day_night.check_day_mode()


