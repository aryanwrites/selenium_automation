from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://blinkit.com")

# --- Step 1: Set location ---
location_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='search delivery location']")))
location_input.click()


location_input.send_keys("Jaypee Institute")


# Wait for suggestions and click the first one
suggestion_container = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "LocationSearchList__LocationListContainer-sc-93rfr7-0"))
)
suggestions = suggestion_container.find_elements(By.XPATH, "./div")
if suggestions:
    suggestions[0].click()
else:
    print("No location suggestions found")

# --- Step 2: Click on search bar wrapper first ---
search_div = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fgHDQx")))
search_div.click()

# --- Step 3: Then target the input inside it ---
search_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "irVxjq")))
# search_input.click(); 
search_input.send_keys("aata")
search_input.send_keys(Keys.ENTER)

first_aata = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//div[@role='button' and @data-pf='reset' and .//div[text()='ADD']]"
)))
first_aata.click()

add_buttons = wait.until(EC.presence_of_all_elements_located((
    By.CLASS_NAME,
    "AddToCart__UpdatedButtonContainer-sc-17ig0e3-0"
)))
add_buttons[0].click()

cart = wait.until(EC.element_to_be_clickable((
    By.CLASS_NAME,
    "gRSsdk"
)))
cart.click();

time.sleep(6)
driver.quit()