<h1 align="left">Reddit UI Automation</h1>

###

<p align="left">
This repository contains automated Selenium-based tests for interacting with Reddit’s user interface. The project is designed to test common Reddit functionalities.
</p>

###

<h2>Project Setup</h2>

<p>Follow the steps below to set up the project and run .</p>

###

<h3>Prerequisites</h3>

<p>Ensure that you have the following installed on your system:</p>

<ul>
  <li>Python </li>
  <li>Chrome browser (or any other browser you plan to use)</li>
  <li>ChromeDriver (or the corresponding driver for your browser)</li>
</ul>

<p>You can download the appropriate version of ChromeDriver <a href="https://chromedriver.chromium.org/downloads">here</a>.</p>

###

<h3>1. Clone the repository</h3>

<p>Start by cloning the repository to your local machine:</p>

<pre><code>git clone https://github.com/atharvlokhande7/reddit-ui-automation.git
cd reddit-ui-automation</code></pre>

###

<h3>2. Install dependencies</h3>

<p>Install the required Python libraries by running:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<p>This will install all necessary dependencies, including Selenium.</p>

###

<h3>3. Configuration</h3>

<h4>config/config.json</h4>

<p>Configure the config.json file located in the config/ directory. This file contains key settings such as the base URL of Reddit, browser choice, and timeout values.</p>

<ul>
  <li><strong>base_url:</strong> The base URL of the site being tested.</li>
  <li><strong>browser:</strong> The browser you wish to use (default is Chrome).</li>
  <li><strong>timeout:</strong> The timeout in seconds for page loading or waiting for elements.</li>
</ul>

<p>Ensure you set the correct browser (e.g., Chrome, Firefox) based on your installed drivers.</p>

<h4>data/test_data.json</h4>

<p>Edit the test_data.json file under the data/ directory. This file stores all necessary test data, including:</p>

<ul>
  <li>Login credentials for valid and invalid login tests.</li>
  <li>Post details for testing content creation.</li>
</ul>

<p>Make sure to replace placeholders like "USERNAME" and "PASSWORD" with actual values for testing.</p>

###

<h3>4. Running the Tests</h3>

<p>Once your configuration is complete, run the tests using the following command:</p>

<pre><code>pytest tests </code></pre>

<p>This will automatically discover and execute all the test cases in the tests/ directory.</p>

###

<h3>5. Browser Configuration</h3>

<p>By default, the tests are configured to run with Chrome. If you wish to use a different browser (e.g., Firefox), change the "browser" setting in config/config.json to your desired browser. Ensure that you have the appropriate WebDriver installed for the chosen browser.</p>

###

<h3>6. Troubleshooting</h3>

<ul>
  <li><strong>ChromeDriver version mismatch:</strong> Ensure that your ChromeDriver version is compatible with your installed version of Google Chrome. You can download the correct version from the ChromeDriver download page.</li>
  <li><strong>Dependency issues:</strong> If you face any issues with dependencies, try upgrading them:</li>
  <pre><code>pip install --upgrade -r requirements.txt</code></pre>
  <li><strong>Driver not found:</strong> If you're using a browser other than Chrome, ensure you have the corresponding WebDriver installed (e.g., GeckoDriver for Firefox).</li>
</ul>
