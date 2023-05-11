# test_suite_api_v1.py

import pytest
import requests
import datasets.reqres_base_keys as api_keys
import datasets.reqres_common_data as reqres
import datasets.reqres_json_objects as api_json

def setup_function(function):
    print("Setup - Test Case: ", function.__doc__)
    
def teardown_function(function):
    print("Teardown - Test Case: ", function.__doc__)


# Get the List of Requests' URLs for REQRES API version 1.

api_v1_urls = reqres.get_sample_requests_urls(reqres.AVAILABLE_API_VERSIONS['v1'])


# SETUP FIXTURE CANDIDATE ?
# Get the List of Responses for REQRES API version 1.

api_response_01 = requests.get(api_v1_urls[api_keys.LIST_USERS])
api_response_02 = requests.get(api_v1_urls[api_keys.SINGLE_USER])
api_response_03 = requests.get(api_v1_urls[api_keys.SINGLE_USER_NOT_FOUND])
api_response_04 = requests.get(api_v1_urls[api_keys.LIST_RESOURCE])
api_response_05 = requests.get(api_v1_urls[api_keys.SINGLE_RESOURCE])
api_response_06 = requests.get(api_v1_urls[api_keys.SINGLE_RESOURCE_NOT_FOUND])

api_request_07_body = api_json.JSON_BODY_REQUEST_CREATE
api_response_07 = requests.post(api_v1_urls[api_keys.CREATE], api_request_07_body)

api_request_08_body = api_json.JSON_BODY_REQUEST_UPDATE_PUT
api_response_08 = requests.put(api_v1_urls[api_keys.UPDATE_PUT], api_request_08_body)

api_request_09_body = api_json.JSON_BODY_REQUEST_UPDATE_PATCH
api_response_09 = requests.patch(api_v1_urls[api_keys.UPDATE_PATCH], api_request_09_body)

api_response_10 = requests.delete(api_v1_urls[api_keys.DELETE])

api_response_11 = requests.post(api_v1_urls[api_keys.REGISTER_SUCCESSFUL], api_json.JSON_BODY_REQUEST_REGISTER_SUCCESSFUL)
api_response_12 = requests.post(api_v1_urls[api_keys.REGISTER_UNSUCCESSFUL], api_json.JSON_BODY_REQUEST_REGISTER_UNSUCCESSFUL)
api_response_13 = requests.post(api_v1_urls[api_keys.LOGIN_SUCCESSFUL], api_json.JSON_BODY_REQUEST_LOGIN_SUCCESSFUL)
api_response_14 = requests.post(api_v1_urls[api_keys.LOGIN_UNSUCCESSFUL], api_json.JSON_BODY_REQUEST_LOGIN_UNSUCCESSFUL)
api_response_15 = requests.get(api_v1_urls[api_keys.DELAYED_RESPONSE])


# TEARDOWN FIXTURE CANDIDATE ?
# Define dictionaries to save results of requests (for comparing results of API and WEB tests)

api_tests_response_codes = {}
api_tests_response_bodies = {}

api_tests_response_codes[api_keys.LIST_USERS] = api_response_01.status_code
api_tests_response_bodies[api_keys.LIST_USERS] = api_response_01.json()

api_tests_response_codes[api_keys.SINGLE_USER] = api_response_02.status_code
api_tests_response_bodies[api_keys.SINGLE_USER] = api_response_02.json()

api_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND] = api_response_03.status_code
api_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND] = api_response_03.json()

api_tests_response_codes[api_keys.LIST_RESOURCE] = api_response_04.status_code
api_tests_response_bodies[api_keys.LIST_RESOURCE] = api_response_04.json()

api_tests_response_codes[api_keys.SINGLE_RESOURCE] = api_response_05.status_code
api_tests_response_bodies[api_keys.SINGLE_RESOURCE] = api_response_05.json()

api_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND] = api_response_06.status_code
api_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND] = api_response_06.json()

api_tests_response_codes[api_keys.CREATE] = api_response_07.status_code
api_tests_response_bodies[api_keys.CREATE] = api_response_07.json()

api_tests_response_codes[api_keys.UPDATE_PUT] = api_response_08.status_code
api_tests_response_bodies[api_keys.UPDATE_PUT] = api_response_08.json()

api_tests_response_codes[api_keys.UPDATE_PATCH] = api_response_09.status_code
api_tests_response_bodies[api_keys.UPDATE_PATCH] = api_response_09.json()

api_tests_response_codes[api_keys.DELETE] = api_response_10.status_code
#api_tests_response_bodies[api_keys.DELETE] = api_response_10.json() # raises JSONDecodeError !!!

api_tests_response_codes[api_keys.REGISTER_SUCCESSFUL] = api_response_11.status_code
api_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL] = api_response_11.json()

api_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL] = api_response_12.status_code
api_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL] = api_response_12.json()

api_tests_response_codes[api_keys.LOGIN_SUCCESSFUL] = api_response_13.status_code
api_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL] = api_response_13.json()

api_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL] = api_response_14.status_code
api_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL] = api_response_14.json()

api_tests_response_codes[api_keys.DELAYED_RESPONSE] = api_response_15.status_code
api_tests_response_bodies[api_keys.DELAYED_RESPONSE] = api_response_15.json()


def print_testing_results(actual_result, expected_result):
    print("\nActual Result: {0}\nExpected Result: {1}\n".format(actual_result, expected_result))

@pytest.mark.parametrize("actual_status_code, expected_status_code",
    [
        (api_tests_response_codes[api_keys.LIST_USERS], reqres.STATUS_CODE_LIST_USERS),
        (api_tests_response_codes[api_keys.SINGLE_USER], reqres.STATUS_CODE_SINGLE_USER),
        (api_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND], reqres.STATUS_CODE_SINGLE_USER_NOT_FOUND),
        (api_tests_response_codes[api_keys.LIST_RESOURCE], reqres.STATUS_CODE_LIST_RESOURCE),
        (api_tests_response_codes[api_keys.SINGLE_RESOURCE], reqres.STATUS_CODE_SINGLE_RESOURCE),
        (api_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND], reqres.STATUS_CODE_SINGLE_RESOURCE_NOT_FOUND),
        (api_tests_response_codes[api_keys.CREATE], reqres.STATUS_CODE_CREATE),
        (api_tests_response_codes[api_keys.UPDATE_PUT], reqres.STATUS_CODE_UPDATE_PUT),
        (api_tests_response_codes[api_keys.UPDATE_PATCH], reqres.STATUS_CODE_UPDATE_PATCH),
        (api_tests_response_codes[api_keys.DELETE], reqres.STATUS_CODE_DELETE),
        (api_tests_response_codes[api_keys.REGISTER_SUCCESSFUL], reqres.STATUS_CODE_REGISTER_SUCCESSFUL),
        (api_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL], reqres.STATUS_CODE_REGISTER_UNSUCCESSFUL),
        (api_tests_response_codes[api_keys.LOGIN_SUCCESSFUL], reqres.STATUS_CODE_LOGIN_SUCCESSFUL),
        (api_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL], reqres.STATUS_CODE_LOGIN_UNSUCCESSFUL),
        (api_tests_response_codes[api_keys.DELAYED_RESPONSE], reqres.STATUS_CODE_DELAYED_RESPONSE)
    ]
)
def test_response_status_code(actual_status_code, expected_status_code):
    """test_response_status_code"""
    print_testing_results(actual_status_code, expected_status_code)
    assert actual_status_code == expected_status_code


@pytest.mark.parametrize("actual_response_body, expected_response_body",
    [
        (api_tests_response_bodies[api_keys.LIST_USERS], api_json.JSON_BODY_RESPONSE_LIST_USERS),
        (api_tests_response_bodies[api_keys.SINGLE_USER], api_json.JSON_BODY_RESPONSE_SINGLE_USER),
        (api_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND], api_json.JSON_BODY_RESPONSE_SINGLE_USER_NOT_FOUND),
        (api_tests_response_bodies[api_keys.LIST_RESOURCE], api_json.JSON_BODY_RESPONSE_LIST_RESOURCE),
        (api_tests_response_bodies[api_keys.SINGLE_RESOURCE], api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE),
        (api_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND], api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE_NOT_FOUND),
        (api_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL], api_json.JSON_BODY_RESPONSE_REGISTER_SUCCESSFUL),
        (api_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL], api_json.JSON_BODY_RESPONSE_REGISTER_UNSUCCESSFUL),
        (api_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL], api_json.JSON_BODY_RESPONSE_LOGIN_SUCCESSFUL),
        (api_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL], api_json.JSON_BODY_RESPONSE_LOGIN_UNSUCCESSFUL),
        (api_tests_response_bodies[api_keys.DELAYED_RESPONSE], api_json.JSON_BODY_RESPONSE_DELAYED)
    ]
)
def test_response_body_object(actual_response_body, expected_response_body):
    """test_response_body_object"""
    print_testing_results(actual_response_body, expected_response_body)
    assert actual_response_body == expected_response_body




actual_response_07_body = api_tests_response_bodies[api_keys.CREATE]
actual_response_08_body = api_tests_response_bodies[api_keys.UPDATE_PUT]
actual_response_09_body = api_tests_response_bodies[api_keys.UPDATE_PATCH]


@pytest.mark.parametrize("actual_attr_value, expected_attr_value",
    [
        (actual_response_07_body[api_json.ATTR_USER_NAME], api_request_07_body[api_json.ATTR_USER_NAME]),
        (actual_response_07_body[api_json.ATTR_USER_JOB], api_request_07_body[api_json.ATTR_USER_JOB]),

        (actual_response_08_body[api_json.ATTR_USER_NAME], api_request_08_body[api_json.ATTR_USER_NAME]),
        (actual_response_08_body[api_json.ATTR_USER_JOB], api_request_08_body[api_json.ATTR_USER_JOB]),
        
        (actual_response_09_body[api_json.ATTR_USER_NAME], api_request_09_body[api_json.ATTR_USER_NAME]),
        (actual_response_09_body[api_json.ATTR_USER_JOB], api_request_09_body[api_json.ATTR_USER_JOB])
    ]
)
def test_user_object_attribute_is_equal(actual_attr_value, expected_attr_value):
    """test_user_object_attribute_is_equal"""
    print_testing_results(actual_attr_value, expected_attr_value)
    assert actual_attr_value == expected_attr_value



# REQUEST_07: CREATE

def test_new_user_id():
    """test_new_user_id"""
    assert int(actual_response_07_body['id']) > 0

def test_new_user_creation_attribute():
    """test_new_user_creation_attribute"""
    assert actual_response_07_body['createdAt'] != ""


# REQUEST_08: UPDATE

def test_put_update_user_updateat_attribute():
    """test_put_update_user_updateat_attribute"""
    assert actual_response_08_body['updatedAt'] != ""


# REQUEST_09: UPDATE

def test_patch_update_user_updateat_attribute():
    """test_patch_update_user_updateat_attribute"""
    assert actual_response_09_body['updatedAt'] != ""
