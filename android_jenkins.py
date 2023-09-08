import time
import os

from appium import webdriver
build_name = os.getenv("LT_BUILD_NAME")
print(build_name)


caps = {

  "lt:options": {
    "w3c": True,
    "tunnel": true,
    "tunnelName": "HelloTESTTUNNEL",
    "deviceName": "Galaxy S23",
    "platformName": "android",
    "platformVersion": "13",
    "isRealMobile": True,
    "app": "prover",
    "build": build_name,
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True,
    # "smartUI.project": "Azure_Pipeline_App_Test"
  }

}


gridUrl = "mobile-hub.lambdatest.com/wd/hub"

username = os.environ.get("LT_USERNAME")
password = os.environ.get("LT_ACCESS_KEY")


url = "https://"+username+":"+password+"@"+gridUrl
driver = webdriver.Remote(desired_capabilities = caps, command_executor = url)
print("driver created")
driver.execute_script("smartui.takeScreenshot=sample-screenshot-1")
driver.execute_script("lambda-status=passed")
time.sleep(17)
driver.quit()
