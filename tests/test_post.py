from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from utils.json_reader import JsonReader

class TestLogin(BaseTest):
    def test_valid_login(self):
        data = JsonReader.read("data/test_data.json")["login"]["valid"]

        # Wait for the username field
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-username"))
        )
        username_field.send_keys(data["username"])

        # Wait for the password field and enter the password
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-password"))
        )
        password_field.send_keys(data["password"])

        # Submit the form (you may need to locate and click the login button)
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Assert that the user is successfully logged in (adjust as per actual behavior)
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Home")  # Replace "Home" with the expected page title
        )
        assert "Home" in self.driver.title
