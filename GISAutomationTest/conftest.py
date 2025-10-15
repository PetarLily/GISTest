import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--username",
        action="store",
        default=None,
        help="Username for authentication"
    )
    parser.addoption(
        "--password",
        action="store",
        default=None,
        help="Password for authentication"
    )


@pytest.fixture
def credentials(request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    return username, password
