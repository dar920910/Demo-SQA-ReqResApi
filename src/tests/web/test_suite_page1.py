# test_suite_page1.py

import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datasets.reqres_base_keys as api_keys
import datasets.reqres_json_objects as api_json
import datasets.reqres_common_data as reqres
import datasets.reqres_web_elements as page


def setup_function(function):
    print("Setup - Test Case: ", function.__doc__)
    
def teardown_function(function):
    print("Teardown - Test Case: ", function.__doc__)


# Configuring Selenium Web Driver for Chrome.

target_options = webdriver.ChromeOptions()
target_options.add_argument('--headless')
driver = webdriver.Chrome(options=target_options)


# Loading REQRES web page.

print("Page loading ...")
driver.set_page_load_timeout(10)
driver.get(reqres.WEBSITE_URL)


# Define dictionaries to save results of requests (for comparing results of WEB and API tests)

web_tests_response_codes = {}
web_tests_response_bodies = {}


# Processing and saving results of every request.

# request_01

request_01_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LIST_USERS)
request_01_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_01 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_01 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LIST_USERS] = int(response_code_01)
web_tests_response_bodies[api_keys.LIST_USERS] = json.loads(response_body_01)

# request_02

request_02_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_USER)
request_02_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_02 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_02 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_USER] = int(response_code_02)
web_tests_response_bodies[api_keys.SINGLE_USER] = json.loads(response_body_02)

# request_03

request_03_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_USER_NOT_FOUND)
request_03_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_03 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_03 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND] = int(response_code_03)
web_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND] = json.loads(response_body_03)

# request_04

request_04_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LIST_RESOURCE)
request_04_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_04 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_04 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LIST_RESOURCE] = int(response_code_04)
web_tests_response_bodies[api_keys.LIST_RESOURCE] = json.loads(response_body_04)

# request_05

request_05_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_RESOURCE)
request_05_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_05 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_05 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_RESOURCE] = int(response_code_05)
web_tests_response_bodies[api_keys.SINGLE_RESOURCE] = json.loads(response_body_05)

# request_06

request_06_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_RESOURCE_NOT_FOUND)
request_06_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_06 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_06 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND] = int(response_code_06)
web_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND] = json.loads(response_body_06)

# request_07

request_07_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_CREATE)
request_07_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_07 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_07 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.CREATE] = int(response_code_07)
web_tests_response_bodies[api_keys.CREATE] = json.loads(response_body_07)

# request_08

request_08_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_UPDATE_PUT)
request_08_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_08 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_08 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.UPDATE_PUT] = int(response_code_08)
web_tests_response_bodies[api_keys.UPDATE_PUT] = json.loads(response_body_08)

# request_09

request_09_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_UPDATE_PATCH)
request_09_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_09 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_09 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.UPDATE_PATCH] = int(response_code_09)
web_tests_response_bodies[api_keys.UPDATE_PATCH] = json.loads(response_body_09)

# request_10

request_10_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_DELETE)
request_10_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_10 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
#response_body_10 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.DELETE] = int(response_code_10)
#web_tests_response_bodies[api_keys.DELETE] = json.loads(response_body_10) # raises JSONDecodeError !!!

# request_11

request_11_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_REGISTER_SUCCESSFUL)
request_11_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_11 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_11 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.REGISTER_SUCCESSFUL] = int(response_code_11)
web_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL] = json.loads(response_body_11)

# request_12

request_12_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_REGISTER_UNSUCCESSFUL)
request_12_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_12 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_12 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL] = int(response_code_12)
web_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL] = json.loads(response_body_12)

# request_13

request_13_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LOGIN_SUCCESSFUL)
request_13_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_13 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_13 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LOGIN_SUCCESSFUL] = int(response_code_13)
web_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL] = json.loads(response_body_13)

# request_14

request_14_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LOGIN_UNSUCCESSFUL)
request_14_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_14 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_14 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL] = int(response_code_14)
web_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL] = json.loads(response_body_14)

# request_15

request_15_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_DELAYED_RESPONSE)
request_15_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_15 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_15 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.DELAYED_RESPONSE] = int(response_code_15)
web_tests_response_bodies[api_keys.DELAYED_RESPONSE] = json.loads(response_body_15)






# REQUEST_01: LIST USERS

def test_get_list_of_users_from_page_to_check_response_code():
    """test_get_list_of_users_from_page_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.LIST_USERS]
    expected_response_code = reqres.STATUS_CODE_LIST_USERS
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_page_to_check_response_body():
    """test_get_list_of_users_from_page_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.LIST_USERS]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LIST_USERS
    assert actual_response_body == expected_response_body

# REQUEST_02: SINGLE USER

def test_get_single_user_by_id_to_check_response_code():
    """test_get_single_user_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.SINGLE_USER]
    expected_response_code = reqres.STATUS_CODE_SINGLE_USER
    assert actual_response_code == expected_response_code

def test_get_single_user_by_id_to_check_response_body():
    """test_get_get_single_user_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.SINGLE_USER]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_USER
    assert actual_response_body == expected_response_body


# REQUEST_03: SINGLE USER NOT FOUND

def test_get_no_existing_single_user_by_id_to_check_response_code():
    """test_get_no_existing_single_user_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND]
    expected_response_code = reqres.STATUS_CODE_SINGLE_USER_NOT_FOUND
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_user_by_id_to_check_response_body():
    """test_get_no_existing_single_user_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_USER_NOT_FOUND
    assert actual_response_body == expected_response_body


# REQUEST_04: LIST RESOURCE

def test_get_list_of_resources_to_check_response_code():
    """test_get_list_of_resources_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.LIST_RESOURCE]
    expected_response_code = reqres.STATUS_CODE_LIST_RESOURCE
    assert actual_response_code == expected_response_code

def test_get_list_of_resources_to_check_response_body():
    """test_get_list_of_resources_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.LIST_RESOURCE]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LIST_RESOURCE
    assert actual_response_body == expected_response_body


# REQUEST_05: SINGLE RESOURCE

def test_get_single_resource_by_id_to_check_response_code():
    """test_get_single_resource_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.SINGLE_RESOURCE]
    expected_response_code = reqres.STATUS_CODE_SINGLE_RESOURCE
    assert actual_response_code == expected_response_code

def test_get_single_resource_by_id_to_check_response_body():
    """test_get_single_resource_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.SINGLE_RESOURCE]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE
    assert actual_response_body == expected_response_body


# REQUEST_06: SINGLE RESOURCE NOT FOUND

def test_get_no_existing_single_resource_by_id_to_check_response_code():
    """test_get_no_existing_single_resource_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    expected_response_code = reqres.STATUS_CODE_SINGLE_RESOURCE_NOT_FOUND
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_resource_by_id_to_check_response_body():
    """test_get_no_existing_single_resource_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE_NOT_FOUND
    assert actual_response_body == expected_response_body


# REQUEST_07: CREATE

def test_create_new_user_to_check_response_code():
    """test_create_new_user_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.CREATE]
    expected_response_code = reqres.STATUS_CODE_CREATE
    assert actual_response_code == expected_response_code

actual_response_07_body = web_tests_response_bodies[api_keys.CREATE]
api_request_07_body = api_json.JSON_BODY_REQUEST_CREATE

def test_new_user_id():
    """test_new_user_id"""
    assert int(actual_response_07_body['id']) > 0

def test_new_user_name_attribute():
    """test_new_user_name_attribute"""
    assert actual_response_07_body['name'] == api_request_07_body['name']

def test_new_user_job_attribute():
    """test_new_user_job_attribute"""
    assert actual_response_07_body['job'] == api_request_07_body['job']

def test_new_user_creation_attribute():
    """test_new_user_creation_attribute"""
    assert actual_response_07_body['createdAt'] != ""


# REQUEST_08: UPDATE

def test_put_update_user_to_check_response_code():
    """test_put_update_user_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.UPDATE_PUT]
    expected_response_code = reqres.STATUS_CODE_UPDATE_PUT
    assert actual_response_code == expected_response_code

actual_response_08_body = web_tests_response_bodies[api_keys.UPDATE_PUT]
api_request_08_body = api_json.JSON_BODY_REQUEST_UPDATE_PUT

def test_put_update_user_name_attribute():
    """test_put_update_user_name_attribute"""
    assert actual_response_08_body['name'] == api_request_08_body['name']

def test_put_update_user_job_attribute():
    """test_put_update_user_job_attribute"""
    assert actual_response_08_body['job'] == api_request_08_body['job']

def test_put_update_user_updateat_attribute():
    """test_put_update_user_updateat_attribute"""
    assert actual_response_08_body['updatedAt'] != ""


# REQUEST_09: UPDATE

def test_patch_update_user_to_check_response_code():
    """test_patch_update_user_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.UPDATE_PATCH]
    expected_response_code = reqres.STATUS_CODE_UPDATE_PATCH
    assert actual_response_code == expected_response_code

actual_response_09_body = web_tests_response_bodies[api_keys.UPDATE_PATCH]
api_request_09_body = api_json.JSON_BODY_REQUEST_UPDATE_PATCH

def test_patch_update_user_name_attribute():
    """test_patch_update_user_name_attribute"""
    assert actual_response_09_body['name'] == api_request_09_body['name']

def test_patch_update_user_job_attribute():
    """test_patch_update_user_job_attribute"""
    assert actual_response_09_body['job'] == api_request_09_body['job']

def test_patch_update_user_updateat_attribute():
    """test_patch_update_user_updateat_attribute"""
    assert actual_response_09_body['updatedAt'] != ""


# REQUEST_10: DELETE

def test_delete_user_by_id_to_check_response_code():
    """test_delete_user_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.DELETE]
    expected_response_code = reqres.STATUS_CODE_DELETE
    assert actual_response_code == expected_response_code


# REQUEST_11: REGISTER SUCCESSFUL

def test_successful_register_to_check_response_code():
    """test_successful_register_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.REGISTER_SUCCESSFUL]
    expected_response_code = reqres.STATUS_CODE_REGISTER_SUCCESSFUL
    assert actual_response_code == expected_response_code

def test_successful_register_to_check_response_body():
    """test_successful_register_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_REGISTER_SUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_12: REGISTER UNSUCCESSFUL

def test_unsuccessful_register_to_check_response_code():
    """test_unsuccessful_register_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL]
    expected_response_code = reqres.STATUS_CODE_REGISTER_UNSUCCESSFUL
    assert actual_response_code == expected_response_code

def test_unsuccessful_register_to_check_response_body():
    """test_unsuccessful_register_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_REGISTER_UNSUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_13: LOGIN SUCCESSFUL

def test_successful_login_to_check_response_code():
    """test_successful_login_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.LOGIN_SUCCESSFUL]
    expected_response_code = reqres.STATUS_CODE_LOGIN_SUCCESSFUL
    assert actual_response_code == expected_response_code

def test_successful_login_to_check_response_body():
    """test_successful_login_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LOGIN_SUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_14: LOGIN UNSUCCESSFUL

def test_unsuccessful_login_to_check_response_code():
    """test_unsuccessful_login_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL]
    expected_response_code = reqres.STATUS_CODE_LOGIN_UNSUCCESSFUL
    assert actual_response_code == expected_response_code

def test_unsuccessful_login_to_check_response_body():
    """test_unsuccessful_login_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LOGIN_UNSUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_15: DELAYED RESPONSE

def test_get_list_of_users_from_the_page_with_delay_to_check_response_code():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_keys.DELAYED_RESPONSE]
    expected_response_code = reqres.STATUS_CODE_DELAYED_RESPONSE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_the_page_with_delay_to_check_response_body():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_keys.DELAYED_RESPONSE]
    expected_response_body = api_json.JSON_BODY_RESPONSE_DELAYED
    assert actual_response_body == expected_response_body
