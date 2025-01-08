from utils.base_test import BaseTest
from utils.json_reader import JsonReader
from selenium.webdriver.common.by import By

class TestLogin(BaseTest):
    def test_valid_login(self):
        data = JsonReader.read("data/test_data.json")["login"]["valid"]
        self.driver.find_element(By.ID, "loginUsername").send_keys(data["username"])
        self.driver.find_element(By.ID, "loginPassword").send_keys(data["password"])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert "Home" in self.driver.title

    def test_invalid_login(self):
        data = JsonReader.read("data/test_data.json")["login"]["invalid"]
        self.driver.find_element(By.ID, "loginUsername").send_keys(data["username"])
        self.driver.find_element(By.ID, "loginPassword").send_keys(data["password"])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        assert "incorrect" in error_message.lower()
