import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.map_page import MapPage
import time


@pytest.mark.usefixtures("driver")
class TestCreateMap:

    def test_create_new_map(self, driver, credentials):
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)
        map_page = MapPage(driver)
        user, password = credentials

        if not login.is_logged_in():
            login.open("https://editor.giscloud.com/")
            login.login(user, password)

        map_name = "AutoMap_" + str(int(time.time()))
        dashboard.create_new_map(map_name)

        time.sleep(1)
        displayed_name = map_page.get_opened_map_name()

        assert map_name in displayed_name, f"Expected map name '{map_name}', got '{displayed_name}'"


