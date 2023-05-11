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

request_01_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LIST_USERS)
request_01_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_01 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_01 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LIST_USERS] = int(response_code_01)
web_tests_response_bodies[api_keys.LIST_USERS] = json.loads(response_body_01)

request_02_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_USER)
request_02_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_02 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_02 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_USER] = int(response_code_02)
web_tests_response_bodies[api_keys.SINGLE_USER] = json.loads(response_body_02)

request_03_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_USER_NOT_FOUND)
request_03_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_03 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_03 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND] = int(response_code_03)
web_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND] = json.loads(response_body_03)

request_04_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LIST_RESOURCE)
request_04_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_04 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_04 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LIST_RESOURCE] = int(response_code_04)
web_tests_response_bodies[api_keys.LIST_RESOURCE] = json.loads(response_body_04)

request_05_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_RESOURCE)
request_05_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_05 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_05 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_RESOURCE] = int(response_code_05)
web_tests_response_bodies[api_keys.SINGLE_RESOURCE] = json.loads(response_body_05)

request_06_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_RESOURCE_NOT_FOUND)
request_06_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_06 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_06 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND] = int(response_code_06)
web_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND] = json.loads(response_body_06)

request_07_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_CREATE)
request_07_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_07 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_07 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.CREATE] = int(response_code_07)
web_tests_response_bodies[api_keys.CREATE] = json.loads(response_body_07)

request_08_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_UPDATE_PUT)
request_08_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_08 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_08 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.UPDATE_PUT] = int(response_code_08)
web_tests_response_bodies[api_keys.UPDATE_PUT] = json.loads(response_body_08)

request_09_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_UPDATE_PATCH)
request_09_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_09 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_09 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.UPDATE_PATCH] = int(response_code_09)
web_tests_response_bodies[api_keys.UPDATE_PATCH] = json.loads(response_body_09)

request_10_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_DELETE)
request_10_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_10 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
web_tests_response_codes[api_keys.DELETE] = int(response_code_10)

request_11_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_REGISTER_SUCCESSFUL)
request_11_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_11 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_11 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.REGISTER_SUCCESSFUL] = int(response_code_11)
web_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL] = json.loads(response_body_11)

request_12_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_REGISTER_UNSUCCESSFUL)
request_12_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_12 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_12 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL] = int(response_code_12)
web_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL] = json.loads(response_body_12)

request_13_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LOGIN_SUCCESSFUL)
request_13_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_13 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_13 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LOGIN_SUCCESSFUL] = int(response_code_13)
web_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL] = json.loads(response_body_13)

request_14_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_LOGIN_UNSUCCESSFUL)
request_14_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_14 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_14 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL] = int(response_code_14)
web_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL] = json.loads(response_body_14)

request_15_sender_element = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_REQUEST_DELAYED_RESPONSE)
request_15_sender_element.click()
time.sleep(page.WAITING_TIMEOUT)
response_code_15 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_CODE).text
response_body_15 = driver.find_element(By.CSS_SELECTOR, page.ELEMENT_CSS_SELECTOR_RESPONSE_BODY).text
web_tests_response_codes[api_keys.DELAYED_RESPONSE] = int(response_code_15)
web_tests_response_bodies[api_keys.DELAYED_RESPONSE] = json.loads(response_body_15)



def setup_module(module):
    print("SETUP: ", module)

def teardown_module(module):
    print("TEARDOWN: ", module)


class TestSuite_WebPage1:
    """TestSuite_WebPage1: This class contains Selenium tests for REQRES main web page."""

    @classmethod
    def setup_class(cls):
        print("\nTEST CLASS SETUP:\n{0}: {1}".format(cls.__name__, cls.__doc__))

    @classmethod
    def teardown_class(cls):
        print("\nTEST CLASS TEARDOWN: {0}\n".format(cls.__name__))

    def setup_method(self, method):
        print("\nSetup Test Method: {0}\n".format(method))

    def teardown_method(self, method):
        print("\nTeardown Test Method: {0}\n".format(method))


    @pytest.mark.parametrize("actual_status_code, expected_status_code",
        [
            (web_tests_response_codes[api_keys.LIST_USERS], reqres.STATUS_CODE_LIST_USERS),
            (web_tests_response_codes[api_keys.SINGLE_USER], reqres.STATUS_CODE_SINGLE_USER),
            (web_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND], reqres.STATUS_CODE_SINGLE_USER_NOT_FOUND),
            (web_tests_response_codes[api_keys.LIST_RESOURCE], reqres.STATUS_CODE_LIST_RESOURCE),
            (web_tests_response_codes[api_keys.SINGLE_RESOURCE], reqres.STATUS_CODE_SINGLE_RESOURCE),
            (web_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND], reqres.STATUS_CODE_SINGLE_RESOURCE_NOT_FOUND),
            (web_tests_response_codes[api_keys.CREATE], reqres.STATUS_CODE_CREATE),
            (web_tests_response_codes[api_keys.UPDATE_PUT], reqres.STATUS_CODE_UPDATE_PUT),
            (web_tests_response_codes[api_keys.UPDATE_PATCH], reqres.STATUS_CODE_UPDATE_PATCH),
            (web_tests_response_codes[api_keys.DELETE], reqres.STATUS_CODE_DELETE),
            (web_tests_response_codes[api_keys.REGISTER_SUCCESSFUL], reqres.STATUS_CODE_REGISTER_SUCCESSFUL),
            (web_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL], reqres.STATUS_CODE_REGISTER_UNSUCCESSFUL),
            (web_tests_response_codes[api_keys.LOGIN_SUCCESSFUL], reqres.STATUS_CODE_LOGIN_SUCCESSFUL),
            (web_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL], reqres.STATUS_CODE_LOGIN_UNSUCCESSFUL),
            (web_tests_response_codes[api_keys.DELAYED_RESPONSE], reqres.STATUS_CODE_DELAYED_RESPONSE)
        ]
    )
    def test_response_status_code(self, actual_status_code, expected_status_code):
        """test_response_status_code"""
        assert actual_status_code == expected_status_code


    @pytest.mark.parametrize("actual_response_body, expected_response_body",
        [
            (web_tests_response_bodies[api_keys.LIST_USERS], api_json.JSON_BODY_RESPONSE_LIST_USERS),
            (web_tests_response_bodies[api_keys.SINGLE_USER], api_json.JSON_BODY_RESPONSE_SINGLE_USER),
            (web_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND], api_json.JSON_BODY_RESPONSE_SINGLE_USER_NOT_FOUND),
            (web_tests_response_bodies[api_keys.LIST_RESOURCE], api_json.JSON_BODY_RESPONSE_LIST_RESOURCE),
            (web_tests_response_bodies[api_keys.SINGLE_RESOURCE], api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE),
            (web_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND], api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE_NOT_FOUND),
            (web_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL], api_json.JSON_BODY_RESPONSE_REGISTER_SUCCESSFUL),
            (web_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL], api_json.JSON_BODY_RESPONSE_REGISTER_UNSUCCESSFUL),
            (web_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL], api_json.JSON_BODY_RESPONSE_LOGIN_SUCCESSFUL),
            (web_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL], api_json.JSON_BODY_RESPONSE_LOGIN_UNSUCCESSFUL),
            (web_tests_response_bodies[api_keys.DELAYED_RESPONSE], api_json.JSON_BODY_RESPONSE_DELAYED)
        ]
    )
    def test_response_body_object(self, actual_response_body, expected_response_body):
        """test_response_body_object"""
        assert actual_response_body == expected_response_body


    @pytest.mark.parametrize("actual_attr_value, expected_attr_value",
        [
            (web_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_NAME], api_json.JSON_BODY_REQUEST_CREATE[api_json.ATTR_USER_NAME]),
            (web_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_JOB], api_json.JSON_BODY_REQUEST_CREATE[api_json.ATTR_USER_JOB]),

            (web_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_NAME], api_json.JSON_BODY_REQUEST_UPDATE_PUT[api_json.ATTR_USER_NAME]),
            (web_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_JOB], api_json.JSON_BODY_REQUEST_UPDATE_PUT[api_json.ATTR_USER_JOB]),

            (web_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_NAME], api_json.JSON_BODY_REQUEST_UPDATE_PATCH[api_json.ATTR_USER_NAME]),
            (web_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_JOB], api_json.JSON_BODY_REQUEST_UPDATE_PATCH[api_json.ATTR_USER_JOB])
        ]
    )
    def test_user_object_attribute_is_equal(self, actual_attr_value, expected_attr_value):
        """test_user_object_attribute_is_equal"""
        assert actual_attr_value == expected_attr_value


    @pytest.mark.parametrize("datetime_attr_value",
        [
            web_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_CREATED],
            web_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_UPDATED],
            web_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_UPDATED]
        ]
    )
    def test_datetime_attribute_is_not_empty(self, datetime_attr_value):
        """test_datetime_attribute_is_not_empty"""
        assert datetime_attr_value != None


    def test_created_user_id_is_positive_value(self):
        """test_created_user_id_is_positive_value"""
        assert int(web_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_ID]) > 0
