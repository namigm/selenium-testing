import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
import allure
from datetime import datetime


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture
def setup(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()


@pytest.fixture
def index_page(setup):
    yield IndexPage(setup)


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failures(setup, request):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        test_case_name = request.node.name
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot = 'screens/screenshot_on_failures' + f'_{test_case_name}' + f'_{formatted_datetime}' + '.png'
        setup.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, 'screenshot_on_failures.png', attachment_type=allure.attachment_type.PNG)