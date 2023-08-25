from selenium.webdriver.common.by import By
from base.base_object import BaseObject


class CheckValidate(BaseObject):
    DATA_INPUT = (By.ID, 'dataInput')
    VALIDATION_SQUARE = (By.ID, 'validationSquare')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_correct_value(self, data, expected_result):
        self.send_keys(locator=self.DATA_INPUT, data=data)
        assert self.get_text(locator=self.VALIDATION_SQUARE) == expected_result
#razdelit