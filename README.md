Reddit UI Automation

This repository contains automated Selenium-based tests for interacting with Reddit’s user interface. The project is designed to test common Reddit functionalities such as login with valid and invalid credentials, as well as posting content.
Project Setup

Follow the steps below to set up the project and run the tests.
Prerequisites

Ensure that you have the following installed on your system:

    Python 3.x

    Chrome browser (or any other browser you plan to use)

    ChromeDriver (or the corresponding driver for your browser)

    You can download the appropriate version of ChromeDriver here.

1. Clone the repository

Start by cloning the repository to your local machine:

git clone https://github.com/your-username/reddit-ui-automation.git
cd reddit-ui-automation

2. Install dependencies

Install the required Python libraries by running:

pip install -r requirements.txt

This will install all necessary dependencies, including Selenium.
3. Configuration
config/config.json

Configure the config.json file located in the config/ directory. This file contains key settings such as the base URL of Reddit, browser choice, and timeout values.

    base_url: The base URL of the site being tested.
    browser: The browser you wish to use (default is Chrome).
    timeout: The timeout in seconds for page loading or waiting for elements.

Ensure you set the correct browser (e.g., Chrome, Firefox) based on your installed drivers.
data/test_data.json

Edit the test_data.json file under the data/ directory. This file stores all necessary test data, including:

    Login credentials for valid and invalid login tests.
    Post details for testing content creation.

Make sure to replace placeholders like "USERNAME" and "PASSWORD" with actual values for testing.
4. Running the Tests

Once your configuration is complete, run the tests using the following command:

pytest

This will automatically discover and execute all the test cases in the tests/ directory.
5. Browser Configuration

By default, the tests are configured to run with Chrome. If you wish to use a different browser (e.g., Firefox), change the "browser" setting in config/config.json to your desired browser. Ensure that you have the appropriate WebDriver installed for the chosen browser.
6. Troubleshooting

    ChromeDriver version mismatch: Ensure that your ChromeDriver version is compatible with your installed version of Google Chrome. You can download the correct version from the ChromeDriver download page.

    Dependency issues: If you face any issues with dependencies, try upgrading them:

pip install --upgrade -r requirements.txt

Driver not found: If you're using a browser other than Chrome, ensure you have the corresponding WebDriver installed (e.g., GeckoDriver for Firefox).
