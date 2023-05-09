# api tests with requests

import json
import pytest
import requests
import tests.api_reqres_v0.api_reqres_v0 as api_reqres_v0


# Define dictionaries to save results of requests (for comparing results of API and WEB tests)

api_tests_response_codes = {}
api_tests_response_bodies = {}


# REQUEST_01: LIST USERS

api_response_01 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_LIST_USERS_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_LIST_USERS_KEY] = api_response_01.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_LIST_USERS_KEY] = api_response_01.json()

def test_get_list_of_users_from_page_to_check_response_code():
    """test_get_list_of_users_from_page_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_LIST_USERS_KEY]
    expected_response_code = api_reqres_v0.API_V0_LIST_USERS_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_page_to_check_response_body():
    """test_get_list_of_users_from_page_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_LIST_USERS_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LIST_USERS_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_02: SINGLE USER

api_response_02 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_USER_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_KEY] = api_response_02.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_KEY] = api_response_02.json()

def test_get_single_user_by_id_to_check_response_code():
    """test_get_single_user_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_USER_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_user_by_id_to_check_response_body():
    """test_get_get_single_user_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_USER_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_03: SINGLE USER NOT FOUND

api_response_03 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY] = api_response_03.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY] = api_response_03.json()

def test_get_no_existing_single_user_by_id_to_check_response_code():
    """test_get_no_existing_single_user_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_user_by_id_to_check_response_body():
    """test_get_no_existing_single_user_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_04: LIST RESOURCE

api_response_04 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_LIST_RESOURCE_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_LIST_RESOURCE_KEY] = api_response_04.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_LIST_RESOURCE_KEY] = api_response_04.json()

def test_get_list_of_resources_to_check_response_code():
    """test_get_list_of_resources_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_LIST_RESOURCE_KEY]
    expected_response_code = api_reqres_v0.API_V0_LIST_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_resources_to_check_response_body():
    """test_get_list_of_resources_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_LIST_RESOURCE_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LIST_RESOURCE_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_05: SINGLE RESOURCE

api_response_05 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_RESOURCE_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY] = api_response_05.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY] = api_response_05.json()

def test_get_single_resource_by_id_to_check_response_code():
    """test_get_single_resource_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_resource_by_id_to_check_response_body():
    """test_get_single_resource_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_RESOURCE_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_06: SINGLE RESOURCE NOT FOUND

api_response_06 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY] = api_response_06.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY] = api_response_06.json()

def test_get_no_existing_single_resource_by_id_to_check_response_code():
    """test_get_no_existing_single_resource_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY]
    expected_response_code = api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_resource_by_id_to_check_response_body():
    """test_get_no_existing_single_resource_by_id_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_07: CREATE

api_request_07_body = json.loads(api_reqres_v0.API_V0_CREATE_REQUEST_BODY)
api_response_07 = requests.post("https://reqres.in" + api_reqres_v0.API_V0_CREATE_REQUEST_URL, api_request_07_body)

api_tests_response_codes[api_reqres_v0.API_V0_CREATE_KEY] = api_response_07.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_CREATE_KEY] = api_response_07.json()

def test_create_new_user_to_check_response_code():
    """test_create_new_user_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_CREATE_KEY]
    expected_response_code = api_reqres_v0.API_V0_CREATE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_07_body = api_tests_response_bodies[api_reqres_v0.API_V0_CREATE_KEY]

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

api_request_08_body = json.loads(api_reqres_v0.API_V0_UPDATE_PUT_REQUEST_BODY)
api_response_08 = requests.put("https://reqres.in" + api_reqres_v0.API_V0_UPDATE_PUT_REQUEST_URL, api_request_08_body)

api_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PUT_KEY] = api_response_08.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PUT_KEY] = api_response_08.json()

def test_put_update_user_to_check_response_code():
    """test_put_update_user_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PUT_KEY]
    expected_response_code = api_reqres_v0.API_V0_UPDATE_PUT_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_08_body = api_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PUT_KEY]

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

api_request_09_body = json.loads(api_reqres_v0.API_V0_UPDATE_PATCH_REQUEST_BODY)
api_response_09 = requests.patch("https://reqres.in" + api_reqres_v0.API_V0_UPDATE_PATCH_REQUEST_URL, api_request_09_body)

api_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PATCH_KEY] = api_response_09.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PATCH_KEY] = api_response_09.json()

def test_patch_update_user_to_check_response_code():
    """test_patch_update_user_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_UPDATE_PATCH_KEY]
    expected_response_code = api_reqres_v0.API_V0_UPDATE_PATCH_RESPONSE_CODE
    assert actual_response_code == expected_response_code

actual_response_09_body = api_tests_response_bodies[api_reqres_v0.API_V0_UPDATE_PATCH_KEY]

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

api_response_10 = requests.delete("https://reqres.in" + api_reqres_v0.API_V0_DELETE_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_DELETE_KEY] = api_response_10.status_code
#api_tests_response_bodies[api_reqres_v0.API_V0_DELETE_KEY] = api_response_10.json() # raises JSONDecodeError !!!

def test_delete_user_by_id_to_check_response_code():
    """test_delete_user_by_id_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_DELETE_KEY]
    expected_response_code = api_reqres_v0.API_V0_DELETE_RESPONSE_CODE
    assert actual_response_code == expected_response_code


# REQUEST_11: REGISTER SUCCESSFUL

api_response_11 = requests.post("https://reqres.in" + api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_REQUEST_URL, json.loads(api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_REQUEST_BODY))

api_tests_response_codes[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY] = api_response_11.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY] = api_response_11.json()

def test_successful_register_to_check_response_code():
    """test_successful_register_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_successful_register_to_check_response_body():
    """test_successful_register_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_12: REGISTER UNSUCCESSFUL

api_response_12 = requests.post("https://reqres.in" + api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_REQUEST_URL, json.loads(api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_REQUEST_BODY))

api_tests_response_codes[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY] = api_response_12.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY] = api_response_12.json()

def test_unsuccessful_register_to_check_response_code():
    """test_unsuccessful_register_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_unsuccessful_register_to_check_response_body():
    """test_unsuccessful_register_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_13: LOGIN SUCCESSFUL

api_response_13 = requests.post("https://reqres.in" + api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_REQUEST_URL, json.loads(api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_REQUEST_BODY))

api_tests_response_codes[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY] = api_response_13.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY] = api_response_13.json()

def test_successful_login_to_check_response_code():
    """test_successful_login_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_successful_login_to_check_response_body():
    """test_successful_login_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_14: LOGIN UNSUCCESSFUL

api_response_14 = requests.post("https://reqres.in" + api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_REQUEST_URL, json.loads(api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_REQUEST_BODY))

api_tests_response_codes[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY] = api_response_14.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY] = api_response_14.json()

def test_unsuccessful_login_to_check_response_code():
    """test_unsuccessful_login_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY]
    expected_response_code = api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_unsuccessful_login_to_check_response_body():
    """test_unsuccessful_login_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_15: DELAYED RESPONSE

api_response_15 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_DELAYED_REQUEST_URL)

api_tests_response_codes[api_reqres_v0.API_V0_DELAYED_KEY] = api_response_15.status_code
api_tests_response_bodies[api_reqres_v0.API_V0_DELAYED_KEY] = api_response_15.json()

def test_get_list_of_users_from_the_page_with_delay_to_check_response_code():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_code"""
    actual_response_code = api_tests_response_codes[api_reqres_v0.API_V0_DELAYED_KEY]
    expected_response_code = api_reqres_v0.API_V0_DELAYED_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_the_page_with_delay_to_check_response_body():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_body"""
    actual_response_body = api_tests_response_bodies[api_reqres_v0.API_V0_DELAYED_KEY]
    expected_response_body = json.loads(api_reqres_v0.API_V0_DELAYED_RESPONSE_BODY)
    assert actual_response_body == expected_response_body
