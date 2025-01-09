from utils.base_test import BaseTest
from utils.json_reader import JsonReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pickle

class TestLogin(BaseTest):
    def test_valid_login(self):
        data = JsonReader.read("data/test_data.json")["login"]["valid"]
        
        login_url = f"{self.base_url}/login"
        self.driver.get(login_url)
        
        # Locate the username and password fields, and submit the login form
        username_field = self.driver.find_element(By.XPATH, "//input[@name='username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        username_field.send_keys(data["username"])
        password_field.send_keys(data["password"])
        password_field.send_keys(Keys.RETURN)
        
        # Wait until the profile image is visible
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='User Avatar']"))
        )
        
        # Save cookies after login
        with open("cookies.pkl", "wb") as file:
            pickle.dump(self.driver.get_cookies(), file)
        
        # Assert login success
        profile_avatar = self.driver.find_element(By.XPATH, "//img[@alt='User Avatar']")
        assert profile_avatar.is_displayed(), "Profile avatar not displayed"
