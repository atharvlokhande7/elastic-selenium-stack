import json
from selenium import webdriver

class BaseTest:
    def setup_method(self):
        # Load configuration from a JSON file
        with open("config/config.json") as config_file:
            config = json.load(config_file)
        
        self.base_url = config["base_url"]  # Ensure base_url is loaded from the config
        
        # Browser setup
        if config["browser"] == "chrome":
            self.driver = webdriver.Chrome()
        elif config["browser"] == "firefox":
            self.driver = webdriver.Firefox()
        
        # Open the base URL
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(config["timeout"])

    def teardown_method(self):
        self.driver.quit()
