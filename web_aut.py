import unittest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import os

build_name = os.getenv("LT_BUILD_NAME")
username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")



class FirstSampleTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.browser_version = "114.0"
        options.platform_name = "Windows 10"
        lt_options = {};
        lt_options["build"] = build_name;
        lt_options["name"] = 'Py-unittest2';
        lt_options["selenium_version"] = "4.0.0";
        lt_options["w3c"] = True;
        lt_options["network"] = 'true';
        options.set_capability('LT:Options', lt_options);
        
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            options=options)
    # tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://lambdatest.com")
        print("Taking screenshot")
        # driver.execute_script("smartui.takeScreenshot,{\"screenshotName\":\"sample-screenshot-1\"}")
        print("screenshot taken successfully")
        driver.execute_script("lambda-status=passed")


if __name__ == "__main__":
    unittest.main()
