import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import env_setup
from pages.index_page import IndexPage
from pages.check_validate import CheckValidate
from pages.input_click import InputClick
import allure
from datetime import datetime
from env_setup import *

@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


# @pytest.fixture
# def setup(get_webdriver):
#     get_webdriver.get(url)
#     yield get_webdriver  # ????
#     get_webdriver.quit()


@pytest.fixture
def index_page(get_webdriver):
    get_webdriver.get(BASE_URL)
    yield IndexPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture
def check_validate(get_webdriver):
    get_webdriver.get(CHECK_VALIDATE_URL)
    yield CheckValidate(get_webdriver)
    get_webdriver.quit()

@pytest.fixture
def input_click(get_webdriver):
    get_webdriver.get(INPUT_CLICK_URL)
    yield InputClick(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failures(get_webdriver, request):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        test_case_name = request.node.name
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot = 'screens/screenshot_on_failures' + f'_{test_case_name}' + f'_{formatted_datetime}' + '.png'
        get_webdriver.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, 'screenshot_on_failures.png', attachment_type=allure.attachment_type.PNG)
