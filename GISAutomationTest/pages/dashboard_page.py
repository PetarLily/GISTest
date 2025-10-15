from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    CREATE_MAP_BTN = (By.ID, "hp_create_map")
    MAP_NAME_INPUT = (By.ID, "mapname")
    MAP_IMAGE = (By.XPATH, "//img[@data-tms='osm']")
    SAVE_MAP_BTN = (By.XPATH, "//button[@onclick='saveMap(false);']")
    MAP_LIST = (By.CSS_SELECTOR, "div.gc-label")

    def create_new_map(self, name):
        self.click(self.CREATE_MAP_BTN)
        self.type(self.MAP_NAME_INPUT, name)
        self.click(self.MAP_IMAGE)
        self.click(self.SAVE_MAP_BTN)

    def is_map_visible(self, name):
        maps = self.driver.find_elements(*self.MAP_LIST)
        return any(name.strip().lower() in m.text.strip().lower() for m in maps)
