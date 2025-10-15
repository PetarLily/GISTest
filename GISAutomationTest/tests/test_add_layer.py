import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.map_page import MapPage
import time


@pytest.mark.usefixtures("driver")
class TestAddLayer:

    def test_add_layer(self, driver, credentials):
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)
        map_page = MapPage(driver)
        user, password = credentials

        login.open("https://editor.giscloud.com/")
        login.login(user, password)

        map_name = "AutoLayerMap_" + str(int(time.time()))
        dashboard.create_new_map(map_name)

        time.sleep(1)
        layer_name = map_page.create_new_layer()

        try:
            assert map_page.is_layer_added(layer_name), f"Layer '{layer_name}' was not added!"
        finally:
            map_page.home()





