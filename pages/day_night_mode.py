from selenium.common import NoSuchElementException
from support.logger import save_log
from pages.index_page import IndexPage
from base.base_object import BaseObject
from selenium.webdriver.common.by import By
from env_setup import WAPP_USER_NAME, WAPP_PASSWORD


class DayNightMode(BaseObject):
    NIGHT_MODE = (By.CSS_SELECTOR, '.night-mode')
    SWITCH_MODE_BTN = (By.CSS_SELECTOR, '.toggle-slider')
    BACK_BTN = (By.CSS_SELECTOR, '.back-button')
    DROP_DOWN_LIST = (By.CSS_SELECTOR, '.dropdown')
    DD_PAGE = (By.LINK_TEXT, "Drag and Drop")
    IC_PAGE = (By.LINK_TEXT, "Input and Click")
    CS_PAGE = (By.LINK_TEXT, "Checkbox and Scroll")
    CV_PAGE = (By.LINK_TEXT, "Check and Validate")
    SV_PAGE = (By.LINK_TEXT, "Sort by")

    LOG = save_log()

    def __init__(self, driver):
        super().__init__(driver)
        self.PAGE_NIGHT_MODE = True
        self.PAGE_DAY_MODE = True

    def is_night_mode_active(self):
        """
        Checking for the night mode
        :return: True in case night mode is active and False if not
        """
        try:
            self.get_element(self.NIGHT_MODE)
            return True
        except NoSuchElementException:
            return False

    def is_day_mode_active(self):
        """
        Checking for the night mode
        :return: True in case day mode is active and False if not
        """
        try:
            self.get_element(self.NIGHT_MODE)
            return False
        except NoSuchElementException:
            return True

    def _click_switch_mode(self):
        """
        just clicking to toggle-slider
        :return:
        """
        self.click(self.SWITCH_MODE_BTN)

    def switch_tonight_mode(self):
        """
        Checking if night mode not active, click to switch to night mode
        :return:
        """
        if not self.is_night_mode_active():
            self._click_switch_mode()
        else:
            pass

    def switch_today_mode(self):
        """
        Checking if day mode not active, click to switch to night mode
        :return:
        """
        if not self.is_day_mode_active():
            self._click_switch_mode()
        else:
            pass

    def page_drag_drop(self):
        """
        function just clicking to drop down list and select page
        :return:
        """
        self.click(self.DROP_DOWN_LIST)
        self.click(self.DD_PAGE)

    def page_input_click(self):
        """
        function just clicking to drop down list and select page
        :return:
        """
        self.click(self.DROP_DOWN_LIST)
        self.click(self.IC_PAGE)

    def page_check_scroll(self):
        """
        function just clicking to drop down list and select page
        :return:
        """
        self.click(self.DROP_DOWN_LIST)
        self.click(self.CS_PAGE)

    def page_check_validate(self):
        """
        function just clicking to drop down list and select page
        :return:
        """
        self.click(self.DROP_DOWN_LIST)
        self.click(self.CV_PAGE)

    def page_sort_by(self):
        """
        function just clicking to drop down list and select page
        :return:
        """
        self.click(self.DROP_DOWN_LIST)
        self.click(self.DD_PAGE)

    def back_button(self):
        """
        function for the clicking back button in order to go back and select next page
        :return:
        """
        self.click(locator=self.BACK_BTN, timeout=15)

    def page_surfing(self, mode):
        """
        function go through all functions and provide value for the page_actions function
        :return:
        """
        for action in [self.page_drag_drop,
                       self.page_input_click,
                       self.page_check_validate,
                       self.page_check_scroll,
                       self.page_sort_by]:
            mode(action)

    def night_page_actions(self, action):
        """
          function accept value from page_surfing function and check page color mode
          :return:
          """
        action()
        if not self.is_night_mode_active():
            self.PAGE_NIGHT_MODE = False
            self.LOG.error(f"{action} not in night mode")
            self.back_button()
        else:
            self.back_button()

    def day_page_actions(self, action):
        """
          function accept value from page_surfing function and check page color mode
          :return:
          """
        action()
        if not self.is_day_mode_active():
            self.PAGE_DAY_MODE = False
            self.LOG.error(f"{action} not in day mode")
            self.back_button()
        else:
            self.back_button()

    def check_night_mode(self):
        """
          encapsulation function
          :assert:
          final state of PAGE_NIGHT_MODE which is defining in page_actions function
          """
        self.switch_tonight_mode()
        index_page = IndexPage(self.driver)
        index_page.login(user_name=WAPP_USER_NAME, password=WAPP_PASSWORD)
        self.page_surfing(self.night_page_actions)
        assert self.PAGE_NIGHT_MODE

    def check_day_mode(self):
        """
          encapsulation function
          :assert:
          final state of PAGE_DAY_MODE which is defining in page_actions function
          """
        self.switch_today_mode()
        index_page = IndexPage(self.driver)
        index_page.login(user_name=WAPP_USER_NAME, password=WAPP_PASSWORD)
        self.page_surfing(self.day_page_actions)
        assert self.PAGE_DAY_MODE
