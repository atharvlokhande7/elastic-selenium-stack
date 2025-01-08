from utils.base_test import BaseTest
from utils.json_reader import JsonReader
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestPostInteraction(BaseTest):
    def test_search_and_comment(self):
        data = JsonReader.read("data/test_data.json")["post"]
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(data["search_keyword"] + Keys.RETURN)

        self.driver.find_element(By.CSS_SELECTOR, ".Post").click()
        comment_box = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        comment_box.send_keys(data["comment_text"])
        self.driver.find_element(By.XPATH, "//button[text()='Comment']").click()

        assert data["comment_text"] in self.driver.page_source
