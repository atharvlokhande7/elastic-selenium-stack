from utils.base_test import BaseTest
from utils.json_reader import JsonReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestLogin(BaseTest):
    def test_valid_login(self):
        data = JsonReader.read("data/test_data.json")["login"]["valid"]
        
        # Locate the actual input fields (username and password)
        username_field = self.driver.find_element(By.XPATH, "//input[@name='username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        
        # Fill in username and password
        username_field.send_keys(data["username"])
        password_field.send_keys(data["password"])
        
        # Press "Enter" to submit the form instead of clicking the button
        password_field.send_keys(Keys.RETURN)
        
        # Wait for a specific element to ensure successful login (e.g., user profile icon)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".profile-avatar"))
        )

        # Check if the profile avatar (or other element) is displayed, indicating a successful login
        profile_avatar = self.driver.find_element(By.CSS_SELECTOR, ".profile-avatar")
        assert profile_avatar.is_displayed()

