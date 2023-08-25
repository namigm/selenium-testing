from base.base_object import BaseObject
from selenium.webdriver.common.by import By
from support.custom_exception import VisibleElementNotFound


class InputClick(BaseObject):
    INPUT_TEXT = (By.ID, 'inputText')
    ADD_BUTTON = (By.ID, 'addBtn')
    ITEMS = (By.CSS_SELECTOR, '#items .item')
    ITEMS2 = (By.ID, 'items')
    DELETE_BUTTON = (By.ID, "deleteBtn")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _input_new_item(self, data):
        self.send_keys(locator=self.INPUT_TEXT, data=data)

    def _click_add_btn(self):
        self.click(self.ADD_BUTTON)

    def _click_remove_btn(self):
        self.click(self.DELETE_BUTTON)

    def _add_new_item(self, data):
        self._input_new_item(data)
        self._click_add_btn()

    def add_item_check(self, data):
        self._add_new_item(data)
        self._check_added_item(data)

    def remove_item_check(self, data):
        self._add_new_item(data)
        self._click_add_btn()
        self._click_remove_btn()
        self._check_removed_item(data)

    def _check_removed_item(self, data):
        try:
            elements = self.get_elements(self.ITEMS2)
            found = any(element.text != data for element in elements)
            removed = found
        except VisibleElementNotFound:
            removed = True
        assert removed, f"Item {data} was removed from the list"

        


    def _check_added_item(self, data):
        elements = self.get_elements(self.ITEMS)
        found = False
        for element in elements:
            if element.text == data:
                found = True
                break
        assert found
