from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("\n*** Welcome to the Sandbox for WEB experiments !!! ***\n")


# Configuring Selenium Web Driver for Chrome.

target_options = webdriver.ChromeOptions()
target_options.add_argument('--headless')
driver = webdriver.Chrome(options=target_options)

# Loading REQRES web page.

print("Page loading ...")
driver.set_page_load_timeout(10)
driver.get('https://reqres.in')


def print_all_elements_of_requests(element_xpath):
    elem = driver.find_element(By.XPATH, element_xpath)
    print(elem.text)

print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[1]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[2]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[3]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[4]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[5]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[6]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[7]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[8]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[9]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[10]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[11]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[12]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[13]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[14]')
print_all_elements_of_requests('//*[@id="console"]/div[1]/ul/li[15]')


# Testing REQRES requests via web browser

def test_request_via_element(element_css_selector, title):
    print("\n\n----- ", title, " -----\n\n")
    request_sender_element = driver.find_element(By.CSS_SELECTOR, element_css_selector)
    request_sender_element.click()
    driver.implicitly_wait(100)

    print("Sleeping...")
    time.sleep(5)

    element = driver.find_element(By.CSS_SELECTOR, ".response-code")
    if element.is_displayed():
        elem = element.text
        print("\nStatus Code: ", elem, '\n')
    else:
        print("ELEMENT is not displayed")

    element = driver.find_element(By.CSS_SELECTOR, ".response > pre")
    if element.is_displayed():
        elem = element.text
        print("\nResponse Body:\n", elem, '\n')
    else:
        print("ELEMENT is not displayed")

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
