from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.custom_exception import VisibleElementNotFound, ClickableElementNotFound
from support.logger import save_log
from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BaseObject:
    LOG = save_log()

    def __init__(self, driver):
        self.driver = driver

    def __wait_element(self, timeout=5):
        """
        Wait for an element
        :param timeout: max timeout to wait
        :return: WebDriverWait class instance with wait setup
        """
        return WebDriverWait(self.driver, timeout)

    def _is_visible(self, locator, timeout=5):
        try:
            visible_element = self.__wait_element(timeout=timeout).until(ec.visibility_of_element_located(locator))
            self.LOG.info(f"Requested element - {locator} is visible")
            return visible_element
        except TimeoutException:
            self.LOG.error(f"Requested element - {locator} isn't visible")
            raise VisibleElementNotFound("Element is not visible")

    def _are_visible(self, locator, timeout=5):
        try:
            visible_elements = self.__wait_element(timeout=timeout).until(
                ec.visibility_of_all_elements_located(locator))
            self.LOG.info(f"Requested elements - {locator} are visible")
            return visible_elements
        except TimeoutException:
            self.LOG.error(f"Requested elements - {locator} are not visible")
            raise VisibleElementNotFound("Elements are not visible")

    def _is_clickable(self, locator, timeout=5):
        try:
            clickable_element = self.__wait_element(timeout=timeout).until(ec.element_to_be_clickable(locator))
            self.LOG.info(f"Requested element - {locator} is clickable")
            return clickable_element
        except TimeoutException:
            self.LOG.error(f"Requested element - {locator} isn't clickable")
            raise ClickableElementNotFound("Element is not visible")

    def send_keys(self, locator, data, timeout=5):
        try:
            self._is_visible(timeout=timeout, locator=locator).send_keys(data)
            self.LOG.info(f"Data - {data} has been sent using element - {locator}")
        except TimeoutException:
            self.LOG.error(f"Data - {data} hasn't been sent using element - {locator}")
            raise VisibleElementNotFound("Element is not visible")

    def click(self, locator, timeout=5):
        try:
            self.LOG.info(f"Element - {locator} has been clicked")
            self._is_clickable(timeout=timeout, locator=locator).click()
        except TimeoutException:
            self.LOG.info(f"Element - {locator} hasn't been clicked")
            raise ClickableElementNotFound("Element is not visible")

    def is_displayed(self, locator, timeout=5):
        try:
            self.LOG.info(f"Element - {locator} is displayed")
            self._is_visible(timeout=timeout, locator=locator)
            return True
        except TimeoutException:
            self.LOG.info(f"Element - {locator} isn't displayed")
            raise VisibleElementNotFound("Element is not visible")

    def get_visible_element(self, locator, timeout=5):
        element = self._is_visible(timeout=timeout, locator=locator)
        self.LOG.info(f"Element - {locator} has been found and visible")
        return element

    def get_elements(self, locator, timeout=5):
        element = self._are_visible(locator=locator, timeout=timeout)
        self.LOG.info(f"Elements - {locator} have been found and visible")
        return element
#####
    def get_element(self, locator):
        element = self.driver.find_element(*locator)
        self.LOG.info(f"Not visible elements - {locator} have been found")
        return element

    def get_text(self, locator, timeout=5):
        element = self._is_visible(timeout=timeout, locator=locator)
        self.LOG.info(f"Text - {locator} has been found and visible")
        return element.text

    def get_items_text(self, locator, timeout=15):
        elements = self._are_visible(timeout=timeout, locator=locator)
        self.LOG.info(f"Texts - {locator} have been found and visible")
        return [element.text for element in elements]

    def drag_drop(self, source, target):
        drag_and_drop(self.driver, self._is_visible(source), self._is_visible(target))

    def move_to_visible_element(self, locator):
        ActionChains(self.driver).move_to_element(self.get_visible_element(locator))

    def select_element(self, locator, text):
        select = Select(self.get_element(locator))
        select.select_by_visible_text(text)
