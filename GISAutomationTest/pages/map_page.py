from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class MapPage(BasePage):
    MAP_TITLE = (By.ID, "map_perm_link")
    ADD_LAYER_BTN = (By.XPATH, "//button[.//span[text()='Add Layer']]")
    FIRST_LAYER_ROW = (By.XPATH, "(//tr[@role='row'][td/i[contains(@class,'fa-file-text-o')]])[1]")
    SELECT_LAYER_BTN = (By.XPATH, "//button[normalize-space(text())='Select']")
    HOME_TAB = (By.ID, "home_tab")

    def get_opened_map_name(self):
        return self.get_text(self.MAP_TITLE)

    def create_new_layer(self):
        self.click(self.ADD_LAYER_BTN)
        self.wait.until(EC.element_to_be_clickable(self.FIRST_LAYER_ROW))
        first_row = self.driver.find_element(*self.FIRST_LAYER_ROW)
        td = first_row.find_element(By.TAG_NAME, "td")
        layer_name_full = td.text.strip()

        if "." in layer_name_full:
            layer_name = layer_name_full.split(".")[0]
        else:
            layer_name = layer_name_full
        first_row.click()

        self.click(self.SELECT_LAYER_BTN)
        return layer_name

    def is_layer_added(self, layer_name):

        layer_locator = (
            By.XPATH, f"//div[@id='layer_list_parent']//li[@rel='layer']//a[contains(text(), '{layer_name}')]")
        try:
            self.wait.until(EC.presence_of_element_located(layer_locator))
            return True
        except:
            return False

    def home(self):
        self.click(self.HOME_TAB)
