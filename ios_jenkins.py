from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

from appium import webdriver
build_name = os.getenv("LT_BUILD_NAME")
print(build_name)

desired_caps = {
    "tunnel": False,
    "tunnelName": os.getenv("LT_TUNNEL_NAME"),
    "deviceName": os.getenv("LT_DEVICE_NAME"),
    "platformName": os.getenv("LT_PLATFORM_NAME"),
    "platformVersion": os.getenv("LT_DEVICE_VERSION"),
    "app": os.getenv("LT_APP_ID"),
    # "deviceName": "iPhone 12",
    # "platformName": "ios",
    # "platformVersion": "14",
    "isRealMobile": True,
    "app": "lt://proverbial-ios",  # Enter app_url here
    "build": build_name,
    "name": "Sample Test - Python",
    "network": True,
    "visual": True,
    "video": True
}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        time.sleep(3)
        colorElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "color")))
        colorElement.click()
        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text")))
        textElement.click()
        toastElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "toast")))
        toastElement.click()
        notification = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "notification")))
        notification.click()
        time.sleep(3)
        geolocation = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "geoLocation")))
        geolocation.click()
        time.sleep(5)
        driver.back()
        home = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Home")))
        home.click()
        speedTest = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "speedTest")))
        speedTest.click()
        time.sleep(5)
        driver.back()
        browser = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Browser")))
        browser.click()
        url = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "url")))
        url.send_keys("https://www.lambdatest.com")
        find = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBsy.ACCESSIBILITY_ID, "find")))
        find.click()
        driver.quit()
    except:
        driver.quit()


startingTest()
