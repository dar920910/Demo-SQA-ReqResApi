from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

print("\n*** Welcome to the Sandbox for Web !!! ***\n")

# Configuring Selenium Web Driver for Chrome.

target_options = webdriver.ChromeOptions()
target_options.add_argument('--headless')
driver = webdriver.Chrome(options=target_options)

# Loading REQRES web page.

print("Page loading ...")
driver.set_page_load_timeout(10)
driver.get('https://reqres.in')


# Testing REQRES requests via web browser

def test_request_via_element(element_css_selector, title):
    print("\n\n----- ", title, " -----\n\n")
    driver.find_element(By.CSS_SELECTOR, element_css_selector)
    driver.implicitly_wait(50)

    status_code_element = WebDriverWait(driver, 10).until(driver.find_element(By.CSS_SELECTOR, ".response-code"))
    response_body_element = WebDriverWait(driver, 10).until(driver.find_element(By.CSS_SELECTOR, ".response > pre"))

    print("\nStatus Code: ", status_code_element.text, '\n')
    print("\nResponse Body:\n", response_body_element.text, '\n')

    driver.implicitly_wait(50) # timeout between the current and next requests

test_request_via_element("li:nth-child(1) > a", "Send Request_01: List Users")
test_request_via_element("li:nth-child(2) > a", "Send Request_02: Single User")
test_request_via_element("li:nth-child(3) > a", "Send Request_03: Single User Not Found")
test_request_via_element("li:nth-child(4) > a", "Send Request_04: List Resource")
test_request_via_element("li:nth-child(5) > a", "Send Request_05: Single Resource")
test_request_via_element("li:nth-child(6) > a", "Send Request_06: Single Resource Not Found")
test_request_via_element("li:nth-child(7) > a", "Send Request_07: Create")
test_request_via_element("li:nth-child(8) > a", "Send Request_08: Update")
test_request_via_element("li:nth-child(9) > a", "Send Request_09: Update")
test_request_via_element("li:nth-child(10) > a", "Send Request_10: Delete")
test_request_via_element("li:nth-child(11) > a", "Send Request_11: Register Successful")
test_request_via_element("li:nth-child(12) > a", "Send Request_12: Register Unsuccessful")
test_request_via_element("li:nth-child(13) > a", "Send Request_13: Login Successful")
test_request_via_element("li:nth-child(14) > a", "Send Request_14: Login Unsuccessful")
test_request_via_element("li:nth-child(15) > a", "Send Request_15: Delayed Response")

driver.quit()