import json
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

with open("links.json", "r") as f:
    data = json.load(f)
    deep_links = data["links"]

    print(f"Total links: {len(deep_links)}")
print(deep_links)

# Appium options
options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "emulator-5554"
options.appPackage = "com.grofers.customerapp"
options.appActivity = "com.grofers.customerapp.activities.SplashActivity"
options.automationName = "UiAutomator2"
options.noReset = True

# Start Appium driver once
driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

for link in deep_links:
    # Ensure app is closed before new deep link
    print("hey")
    driver.terminate_app("com.grofers.customerapp")
    time.sleep(1)

    # Relaunch using deep link
    driver.execute_script("mobile: deepLink", {
        "url": link,
        "package": "com.grofers.customerapp"
    })

    time.sleep(5)  # Allow screen to load

    try:
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("Add")'
            ))
        )
        add_to_cart_button.click()
    except Exception as e:
        print(f"❌ Failed to add item from: {link} | Error: {e}")

    time.sleep(2)

driver.quit()