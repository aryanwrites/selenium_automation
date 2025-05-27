from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
import time

options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "emulator-5554"
options.appPackage = "com.grofers.customerapp"
options.appActivity = "com.grofers.customerapp.activities.SplashActivity"
options.automationName = "UiAutomator2"

options.noReset = True

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)

driver.execute_script("mobile: deepLink", {
    "url": "https://blinkit.onelink.me/z75u/9i0ekay9",
    "package": "com.grofers.customerapp"
})

try:
    wait = WebDriverWait(driver, 8)
    add_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='Add to Cart']"))
    )
    add_button.click()
    print("✅ 'Add to Cart' button clicked successfully.")
except Exception as e:
    print("Failed to click 'Add to Cart':", e)

# Optional: pause and quit
time.sleep(3)

driver.quit()