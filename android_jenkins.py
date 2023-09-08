import time
import os

from appium import webdriver
build_name = os.getenv("LT_BUILD_NAME")
print(build_name)


caps = {

  "lt:options": {
    "w3c": True,
    "tunnel": False,
    "tunnelName": "HelloTESTTUNNEL",
    # "deviceName": "Galaxy S23",
    # "platformName": "android",
    # "platformVersion": "13",
    # "app": "prover",
    # "tunnelName": os.getenv("LT_TUNNEL_NAME"),
    "deviceName": os.getenv("LT_DEVICE_NAME"),
    "platformName": os.getenv("LT_PLATFORM_NAME"),
    "platformVersion": os.getenv("LT_DEVICE_VERSION"),
    "app": os.getenv("LT_APP_ID"),
    "isRealMobile": True,
    
    
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
time.sleep(25)
driver.quit()
