from base.base_object import BaseObject
from selenium.webdriver.common.by import By


class DragDrop(BaseObject):
    DRAG_DROPS_PAIRS = [((By.CSS_SELECTOR, "#item-3"), (By.CSS_SELECTOR, "#item-1")),
                        ((By.CSS_SELECTOR, "#item-2"), (By.CSS_SELECTOR, "#item-1")),
                        ((By.CSS_SELECTOR, "#item-7"), (By.CSS_SELECTOR, "#item-1")),
                        ((By.CSS_SELECTOR, "#item-4"), (By.CSS_SELECTOR, "#item-1"))
                        ]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def dr_testing(self):
        for source_element, target_element in self.DRAG_DROPS_PAIRS:
            self.drag_drop(source_element, target_element)
