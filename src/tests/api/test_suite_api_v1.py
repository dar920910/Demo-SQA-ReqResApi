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



# REQUEST_01: LIST USERS

def test_get_list_of_users_from_page_to_check_response_code():
    """test_get_list_of_users_from_page_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.LIST_USERS]
    expected_response_code = reqres.API_V0_LIST_USERS_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_page_to_check_response_body():
    """test_get_list_of_users_from_page_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.LIST_USERS]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LIST_USERS
    assert actual_response_body == expected_response_body


# REQUEST_02: SINGLE USER

def test_get_single_user_by_id_to_check_response_code():
    """test_get_single_user_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.SINGLE_USER]
    expected_response_code = reqres.API_V0_SINGLE_USER_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_user_by_id_to_check_response_body():
    """test_get_get_single_user_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.SINGLE_USER]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_USER
    assert actual_response_body == expected_response_body


# REQUEST_03: SINGLE USER NOT FOUND

def test_get_no_existing_single_user_by_id_to_check_response_code():
    """test_get_no_existing_single_user_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND]
    expected_response_code = reqres.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_user_by_id_to_check_response_body():
    """test_get_no_existing_single_user_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_USER_NOT_FOUND
    assert actual_response_body == expected_response_body


# REQUEST_04: LIST RESOURCE

def test_get_list_of_resources_to_check_response_code():
    """test_get_list_of_resources_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.LIST_RESOURCE]
    expected_response_code = reqres.API_V0_LIST_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_resources_to_check_response_body():
    """test_get_list_of_resources_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.LIST_RESOURCE]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LIST_RESOURCE
    assert actual_response_body == expected_response_body


# REQUEST_05: SINGLE RESOURCE

def test_get_single_resource_by_id_to_check_response_code():
    """test_get_single_resource_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.SINGLE_RESOURCE]
    expected_response_code = reqres.API_V0_SINGLE_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_resource_by_id_to_check_response_body():
    """test_get_single_resource_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.SINGLE_RESOURCE]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE
    assert actual_response_body == expected_response_body


# REQUEST_06: SINGLE RESOURCE NOT FOUND

def test_get_no_existing_single_resource_by_id_to_check_response_code():
    """test_get_no_existing_single_resource_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    expected_response_code = reqres.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_resource_by_id_to_check_response_body():
    """test_get_no_existing_single_resource_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    expected_response_body = api_json.JSON_BODY_RESPONSE_SINGLE_RESOURCE_NOT_FOUND
    assert actual_response_body == expected_response_body


# REQUEST_07: CREATE

def test_create_new_user_to_check_response_code():
    """test_create_new_user_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.CREATE]
    expected_response_code = reqres.API_V0_CREATE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_07_body = api_tests_response_bodies[api_keys.CREATE]

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
    actual_response_code = api_tests_response_codes[api_keys.UPDATE_PUT]
    expected_response_code = reqres.API_V0_UPDATE_PUT_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_08_body = api_tests_response_bodies[api_keys.UPDATE_PUT]

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
    actual_response_code = api_tests_response_codes[api_keys.UPDATE_PATCH]
    expected_response_code = reqres.API_V0_UPDATE_PATCH_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_09_body = api_tests_response_bodies[api_keys.UPDATE_PATCH]

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
    actual_response_code = api_tests_response_codes[api_keys.DELETE]
    expected_response_code = reqres.API_V0_DELETE_RESPONSE_CODE
    assert actual_response_code == expected_response_code


# REQUEST_11: REGISTER SUCCESSFUL

def test_successful_register_to_check_response_code():
    """test_successful_register_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.REGISTER_SUCCESSFUL]
    expected_response_code = reqres.API_V0_REGISTER_SUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_successful_register_to_check_response_body():
    """test_successful_register_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_REGISTER_SUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_12: REGISTER UNSUCCESSFUL

def test_unsuccessful_register_to_check_response_code():
    """test_unsuccessful_register_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL]
    expected_response_code = reqres.API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_unsuccessful_register_to_check_response_body():
    """test_unsuccessful_register_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_REGISTER_UNSUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_13: LOGIN SUCCESSFUL

def test_successful_login_to_check_response_code():
    """test_successful_login_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.LOGIN_SUCCESSFUL]
    expected_response_code = reqres.API_V0_LOGIN_SUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_successful_login_to_check_response_body():
    """test_successful_login_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LOGIN_SUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_14: LOGIN UNSUCCESSFUL

def test_unsuccessful_login_to_check_response_code():
    """test_unsuccessful_login_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL]
    expected_response_code = reqres.API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_unsuccessful_login_to_check_response_body():
    """test_unsuccessful_login_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL]
    expected_response_body = api_json.JSON_BODY_RESPONSE_LOGIN_UNSUCCESSFUL
    assert actual_response_body == expected_response_body


# REQUEST_15: DELAYED RESPONSE

def test_get_list_of_users_from_the_page_with_delay_to_check_response_code():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_keys.DELAYED_RESPONSE]
    expected_response_code = reqres.API_V0_DELAYED_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_the_page_with_delay_to_check_response_body():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_keys.DELAYED_RESPONSE]
    expected_response_body = api_json.JSON_BODY_RESPONSE_DELAYED
    assert actual_response_body == expected_response_body
