from selenium import webdriver
import json

class BaseTest:
    def setup_method(self):
        with open("config/config.json") as config_file:
            config = json.load(config_file)
        if config["browser"] == "chrome":
            self.driver = webdriver.Chrome()
        elif config["browser"] == "firefox":
            self.driver = webdriver.Firefox()
        self.driver.get(config["base_url"])
        self.driver.implicitly_wait(config["timeout"])

    def teardown_method(self):
        self.driver.quit()
