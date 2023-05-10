# test_suite_page1.py

import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tests.api_reqres_v0.api_reqres_v0 as api_reqres_v0


# Configuring Selenium Web Driver for Chrome.

target_options = webdriver.ChromeOptions()
target_options.add_argument('--headless')
driver = webdriver.Chrome(options=target_options)


# Loading REQRES web page.

print("Page loading ...")
driver.set_page_load_timeout(10)
driver.get('https://reqres.in')


# Define dictionaries to save results of requests (for comparing results of WEB and API tests)

web_tests_response_codes = {}
web_tests_response_bodies = {}


# Processing and saving results of every request.

# request_01

request_01_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_LIST_USERS_SENDER_ELEMENT_CSS_SELECTOR)
request_01_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_01 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_01 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_LIST_USERS_KEY] = int(response_code_01)
web_tests_response_bodies[api_reqres_v0.API_V0_LIST_USERS_KEY] = json.loads(response_body_01)

# request_02

request_02_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_SINGLE_USER_SENDER_ELEMENT_CSS_SELECTOR)
request_02_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_02 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_02 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_KEY] = int(response_code_02)
web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_KEY] = json.loads(response_body_02)

# request_03

request_03_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_SENDER_ELEMENT_CSS_SELECTOR)
request_03_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_03 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_03 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY] = int(response_code_03)
web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY] = json.loads(response_body_03)

# request_04

request_04_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_LIST_RESOURCE_SENDER_ELEMENT_CSS_SELECTOR)
request_04_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_04 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_04 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_LIST_RESOURCE_KEY] = int(response_code_04)
web_tests_response_bodies[api_reqres_v0.API_V0_LIST_RESOURCE_KEY] = json.loads(response_body_04)

# request_05

request_05_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_SINGLE_RESOURCE_SENDER_ELEMENT_CSS_SELECTOR)
request_05_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_05 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_05 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY] = int(response_code_05)
web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY] = json.loads(response_body_05)

# request_06

request_06_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_SENDER_ELEMENT_CSS_SELECTOR)
request_06_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_06 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_06 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY] = int(response_code_06)
web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY] = json.loads(response_body_06)

# request_07

request_07_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_CREATE_SENDER_ELEMENT_CSS_SELECTOR)
request_07_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_07 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_07 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_CREATE_KEY] = int(response_code_07)
web_tests_response_bodies[api_reqres_v0.API_V0_CREATE_KEY] = json.loads(response_body_07)

# request_08

request_08_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_UPDATE_PUT_SENDER_ELEMENT_CSS_SELECTOR)
request_08_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_08 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_08 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PUT_KEY] = int(response_code_08)
web_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PUT_KEY] = json.loads(response_body_08)

# request_09

request_09_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_UPDATE_PATCH_SENDER_ELEMENT_CSS_SELECTOR)
request_09_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_09 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_09 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PATCH_KEY] = int(response_code_09)
web_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PATCH_KEY] = json.loads(response_body_09)

# request_10

request_10_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_DELETE_SENDER_ELEMENT_CSS_SELECTOR)
request_10_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_10 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
#response_body_10 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_DELETE_KEY] = int(response_code_10)
#web_tests_response_bodies[api_reqres_v0.API_V0_DELETE_KEY] = json.loads(response_body_10) # raises JSONDecodeError !!!

# request_11

request_11_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR)
request_11_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_11 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_11 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY] = int(response_code_11)
web_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY] = json.loads(response_body_11)

# request_12

request_12_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR)
request_12_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_12 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_12 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY] = int(response_code_12)
web_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY] = json.loads(response_body_12)

# request_13

request_13_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR)
request_13_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_13 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_13 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY] = int(response_code_13)
web_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY] = json.loads(response_body_13)

# request_14

request_14_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR)
request_14_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_14 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_14 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY] = int(response_code_14)
web_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY] = json.loads(response_body_14)

# request_15

request_15_sender_element = driver.find_element(By.CSS_SELECTOR, api_reqres_v0.API_V0_DELAYED_SENDER_ELEMENT_CSS_SELECTOR)
request_15_sender_element.click()
driver.implicitly_wait(100)
time.sleep(5)
response_code_15 = driver.find_element(By.CSS_SELECTOR, ".response-code").text
response_body_15 = driver.find_element(By.CSS_SELECTOR, ".response > pre").text
web_tests_response_codes[api_reqres_v0.API_V0_DELAYED_KEY] = int(response_code_15)
web_tests_response_bodies[api_reqres_v0.API_V0_DELAYED_KEY] = json.loads(response_body_15)






# REQUEST_01: LIST USERS

def test_get_list_of_users_from_page_to_check_response_code():
    """test_get_list_of_users_from_page_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_LIST_USERS_KEY]
    expected_response_code = api_reqres_v0.API_V0_LIST_USERS_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_page_to_check_response_body():
    """test_get_list_of_users_from_page_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_LIST_USERS_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LIST_USERS_RESPONSE_BODY)
    assert actual_response_body == expected_response_body

# REQUEST_02: SINGLE USER

def test_get_single_user_by_id_to_check_response_code():
    """test_get_single_user_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_USER_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_user_by_id_to_check_response_body():
    """test_get_get_single_user_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_USER_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_03: SINGLE USER NOT FOUND

def test_get_no_existing_single_user_by_id_to_check_response_code():
    """test_get_no_existing_single_user_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_user_by_id_to_check_response_body():
    """test_get_no_existing_single_user_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_04: LIST RESOURCE

def test_get_list_of_resources_to_check_response_code():
    """test_get_list_of_resources_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_LIST_RESOURCE_KEY]
    expected_response_code = api_reqres_v0.API_V0_LIST_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_resources_to_check_response_body():
    """test_get_list_of_resources_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_LIST_RESOURCE_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LIST_RESOURCE_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_05: SINGLE RESOURCE

def test_get_single_resource_by_id_to_check_response_code():
    """test_get_single_resource_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_resource_by_id_to_check_response_body():
    """test_get_single_resource_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_RESOURCE_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_06: SINGLE RESOURCE NOT FOUND

def test_get_no_existing_single_resource_by_id_to_check_response_code():
    """test_get_no_existing_single_resource_by_id_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_resource_by_id_to_check_response_body():
    """test_get_no_existing_single_resource_by_id_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_07: CREATE

def test_create_new_user_to_check_response_code():
    """test_create_new_user_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_CREATE_KEY]
    expected_response_code = api_reqres_v0.API_V0_CREATE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_07_body = web_tests_response_bodies[api_reqres_v0.API_V0_CREATE_KEY]
api_request_07_body = json.loads(api_reqres_v0.API_V0_CREATE_REQUEST_BODY)

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
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PUT_KEY]
    expected_response_code = api_reqres_v0.API_V0_UPDATE_PUT_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_08_body = web_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PUT_KEY]
api_request_08_body = json.loads(api_reqres_v0.API_V0_UPDATE_PUT_REQUEST_BODY)

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
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PATCH_KEY]
    expected_response_code = api_reqres_v0.API_V0_UPDATE_PATCH_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_09_body = web_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PATCH_KEY]
api_request_09_body = json.loads(api_reqres_v0.API_V0_UPDATE_PATCH_REQUEST_BODY)

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
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_DELETE_KEY]
    expected_response_code = api_reqres_v0.API_V0_DELETE_RESPONSE_CODE
    assert actual_response_code == expected_response_code


# REQUEST_11: REGISTER SUCCESSFUL

def test_successful_register_to_check_response_code():
    """test_successful_register_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_successful_register_to_check_response_body():
    """test_successful_register_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_12: REGISTER UNSUCCESSFUL

def test_unsuccessful_register_to_check_response_code():
    """test_unsuccessful_register_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_unsuccessful_register_to_check_response_body():
    """test_unsuccessful_register_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_13: LOGIN SUCCESSFUL

def test_successful_login_to_check_response_code():
    """test_successful_login_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_successful_login_to_check_response_body():
    """test_successful_login_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_14: LOGIN UNSUCCESSFUL

def test_unsuccessful_login_to_check_response_code():
    """test_unsuccessful_login_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_unsuccessful_login_to_check_response_body():
    """test_unsuccessful_login_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_15: DELAYED RESPONSE

def test_get_list_of_users_from_the_page_with_delay_to_check_response_code():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_code"""
    actual_response_code = web_tests_response_codes[api_reqres_v0.API_V0_DELAYED_KEY]
    expected_response_code = api_reqres_v0.API_V0_DELAYED_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_the_page_with_delay_to_check_response_body():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_body"""
    actual_response_body = web_tests_response_bodies[api_reqres_v0.API_V0_DELAYED_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_DELAYED_RESPONSE_BODY)
    assert actual_response_body == expected_response_body