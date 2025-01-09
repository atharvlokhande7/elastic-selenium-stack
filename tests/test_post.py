from utils.base_test import BaseTest
from utils.json_reader import JsonReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestPost(BaseTest):
    def setup_method(self):
        # Make sure the BaseTest driver is set up first
        super().setup_method()  # Initialize the driver and base URL

        # Now, load cookies before performing the test
        with open("cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
        
        # Go to the base URL to ensure we are on the correct page
        self.driver.get(self.base_url)
        
        # Add cookies to the driver
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        
        # Refresh the page to ensure the cookies are applied
        self.driver.refresh()

    def test_create_post(self):
        # Load the data for the post from the JSON file
        data = JsonReader.read("data/test_data.json")["post"]["valid"]
        
        # Wait for the page to load fully and ensure we are logged in
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Create')]"))
        )

        # Locate and click the "Create" button
        create_button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Create')]")
        create_button.click()

        # Wait for the title field to appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "title"))
        )

        # Locate the title and body fields
        title_field = self.driver.find_element(By.NAME, "title")
        body_field = self.driver.find_element(By.XPATH, "//div[@slot='rte'][@contenteditable='true']")

        # Fill out the title and body
        title_field.send_keys(data["title"])
        body_field.send_keys(data["content"])

        # Wait for the dropdown icon to appear and click it
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@slot='dropdown-icon']"))
        )
        dropdown_button = self.driver.find_element(By.XPATH, "//div[@slot='dropdown-icon']")
        actions = ActionChains(self.driver)
        actions.click(dropdown_button)  # Click the dropdown
        actions.send_keys("u/test_the_process")  
        actions.perform()  # Execute the actions
        time.sleep(2)  # Adjust the sleep time as needed

        # Now, send the down arrow and enter key
        actions = ActionChains(self.driver)

        actions.send_keys(Keys.DOWN)
        actions.perform()  # Execute the actions

        time.sleep(1)  # Adjust the sleep time as needed

        actions.send_keys(Keys.RETURN)
        actions.perform()  # Execute the actions

        # Wait for the "Your profile" span element to be visible


        # Wait for the submit button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit-post-button"))
        )

        # Locate and click the submit button
        submit_button = self.driver.find_element(By.ID, "submit-post-button")
        submit_button.click()

        # Wait for the post to appear on the user's feed
        time.sleep(5)

        # Add assertions to verify the post was created
        assert data["title"] in self.driver.page_source
        assert data["content"] in self.driver.page_source
