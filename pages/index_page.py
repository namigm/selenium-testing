import allure
from selenium.webdriver.common.by import By
from base.base_object import BaseObject


class IndexPage(BaseObject):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CLASS_NAME, "login-button")
    LOGOUT_BTN = (By.CLASS_NAME, "logout-button")
    MESSAGE_FIELD = (By.ID,"message")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self,user_name,password):
        self.__enter_username(user_name)
        self.__enter_password(password)
        self.__click_login_btn()

    @allure.step("entering username")  # ?
    def __enter_username(self, user_name):
        self.send_keys(locator=self.USERNAME_FIELD, data=user_name, timeout=25)
        # self.send_keys(locator=self.USERNAME_FIELD, data="correct_username", timeout=25)

    @allure.step("entering password")
    def __enter_password(self, password):
        # self.send_keys(self.PASSWORD_FIELD, "correct_password")
        self.send_keys(self.PASSWORD_FIELD, password)

    @allure.step("clicking to log in button")
    def __click_login_btn(self):
        self.click(self.LOGIN_BTN)

    @allure.step("verifying that log in was successful")
    def is_logged_in(self):
        assert self.is_displayed(locator=self.LOGOUT_BTN,
                                 timeout=25), f"Element {self.LOGOUT_BTN} is not displayed on the page"

    @allure.step("checking error message")
    def check_error_message(self, expected_result):
        element_text = self.get_text(self.MESSAGE_FIELD)
        assert element_text == expected_result, f'Expected: {element_text} but received: {expected_result}'






