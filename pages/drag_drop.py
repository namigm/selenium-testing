from base.base_object import BaseObject
from selenium.webdriver.common.by import By


class DragDrop(BaseObject):
    DRAG_DROPS_PAIRS = [((By.CSS_SELECTOR, "#item-3"), (By.CSS_SELECTOR, "#item-1")),
                        ((By.CSS_SELECTOR, "#item-2"), (By.CSS_SELECTOR, "#item-1")),
                        ((By.CSS_SELECTOR, "#item-7"), (By.CSS_SELECTOR, "#item-1")),
                        ((By.CSS_SELECTOR, "#item-4"), (By.CSS_SELECTOR, "#item-1")),
                        ((By.CSS_SELECTOR, "#item-6"), (By.CSS_SELECTOR, "#item-5"))
                        ]
    DONE_BTN = (By.CSS_SELECTOR, ".done")
    LETTERS = (By.CSS_SELECTOR, ".item")
    EXPECTED_LETTER_ORDERS = ['T', 'E', 'S', 'T', 'I', 'N', 'G']

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def dr_testing(self):
        for source_element, target_element in self.DRAG_DROPS_PAIRS:
            self.drag_drop(source_element, target_element)

    def check_done_btn(self):
        assert self.get_element(self.DONE_BTN)

    def check_sequence(self):
        assert self.get_items_text(self.LETTERS) == self.EXPECTED_LETTER_ORDERS
