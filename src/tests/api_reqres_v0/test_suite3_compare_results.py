import json
import pytest
import requests
import tests.api_reqres_v0.api_reqres_v0 as api_reqres_v0
import tests.api_reqres_v0.test_suite1_reqres_api as test_suite1_reqres_api
import tests.api_reqres_v0.test_suite2_reqres_web as test_suite2_reqres_web


# Define requests' keys for using in tests.

req_01_key = api_reqres_v0.API_V0_LIST_USERS_KEY
req_02_key = api_reqres_v0.API_V0_SINGLE_USER_KEY
req_03_key = api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_KEY
req_04_key = api_reqres_v0.API_V0_LIST_RESOURCE_KEY
req_05_key = api_reqres_v0.API_V0_SINGLE_RESOURCE_KEY
req_06_key = api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY
req_07_key = api_reqres_v0.API_V0_CREATE_KEY
req_08_key = api_reqres_v0.API_V0_UPDATE_PUT_KEY
req_09_key = api_reqres_v0.API_V0_UPDATE_PATCH_KEY
req_10_key = api_reqres_v0.API_V0_DELETE_KEY
req_11_key = api_reqres_v0.API_V0_REGISTER_SUCCESSFUL_KEY
req_12_key = api_reqres_v0.API_V0_REGISTER_UNSUCCESSFUL_KEY
req_13_key = api_reqres_v0.API_V0_LOGIN_SUCCESSFUL_KEY
req_14_key = api_reqres_v0.API_V0_LOGIN_UNSUCCESSFUL_KEY
req_15_key = api_reqres_v0.API_V0_DELAYED_KEY

# Define aliases of dictionaries keys for using in tests.

api_resp_codes = test_suite1_reqres_api.api_tests_response_codes
api_resp_bodies = test_suite1_reqres_api.api_tests_response_bodies
web_resp_codes = test_suite2_reqres_web.web_tests_response_codes
web_resp_bodies = test_suite2_reqres_web.web_tests_response_bodies



# REQUEST_01: LIST USERS

def test_compare_for_get_list_of_users_from_page_to_check_response_code():
    """test_compare_for_get_list_of_users_from_page_to_check_response_code"""
    api_status_code = api_resp_codes[req_01_key]
    web_status_code = web_resp_codes[req_01_key]
    assert api_status_code == web_status_code

def test_compare_for_get_list_of_users_from_page_to_check_response_body():
    """test_compare_for_get_list_of_users_from_page_to_check_response_body"""
    api_response_body = api_resp_bodies[req_01_key]
    web_response_body = web_resp_bodies[req_01_key]
    assert api_response_body == web_response_body

# REQUEST_02: SINGLE USER

def test_compare_for_get_single_user_by_id_to_check_response_code():
    """test_compare_for_get_single_user_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[req_02_key]
    web_status_code = web_resp_codes[req_02_key]
    assert api_status_code == web_status_code

def test_compare_for_get_single_user_by_id_to_check_response_body():
    """test_compare_for_get_get_single_user_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[req_02_key]
    web_response_body = web_resp_bodies[req_02_key]
    assert api_response_body == web_response_body


# REQUEST_03: SINGLE USER NOT FOUND

def test_compare_for_get_no_existing_single_user_by_id_to_check_response_code():
    """test_compare_for_get_no_existing_single_user_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[req_03_key]
    web_status_code = web_resp_codes[req_03_key]
    assert api_status_code == web_status_code

def test_compare_for_get_no_existing_single_user_by_id_to_check_response_body():
    """test_compare_for_get_no_existing_single_user_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[req_03_key]
    web_response_body = web_resp_bodies[req_03_key]
    assert api_response_body == web_response_body


# REQUEST_04: LIST RESOURCE

def test_compare_for_get_list_of_resources_to_check_response_code():
    """test_compare_for_get_list_of_resources_to_check_response_code"""
    api_status_code = api_resp_codes[req_04_key]
    web_status_code = web_resp_codes[req_04_key]
    assert api_status_code == web_status_code

def test_compare_for_get_list_of_resources_to_check_response_body():
    """test_compare_for_get_list_of_resources_to_check_response_body"""
    api_response_body = api_resp_bodies[req_04_key]
    web_response_body = web_resp_bodies[req_04_key]
    assert api_response_body == web_response_body


# REQUEST_05: SINGLE RESOURCE

def test_compare_for_get_single_resource_by_id_to_check_response_code():
    """test_compare_for_get_single_resource_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[req_05_key]
    web_status_code = web_resp_codes[req_05_key]
    assert api_status_code == web_status_code

def test_compare_for_get_single_resource_by_id_to_check_response_body():
    """test_compare_for_get_single_resource_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[req_05_key]
    web_response_body = web_resp_bodies[req_05_key]
    assert api_response_body == web_response_body


# REQUEST_06: SINGLE RESOURCE NOT FOUND

def test_compare_for_get_no_existing_single_resource_by_id_to_check_response_code():
    """test_compare_for_get_no_existing_single_resource_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[req_06_key]
    web_status_code = web_resp_codes[req_06_key]
    assert api_status_code == web_status_code

def test_compare_for_get_no_existing_single_resource_by_id_to_check_response_body():
    """test_compare_for_get_no_existing_single_resource_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[req_06_key]
    web_response_body = web_resp_bodies[req_06_key]
    assert api_response_body == web_response_body


# REQUEST_07: CREATE

def test_compare_for_create_new_user_to_check_response_code():
    """test_compare_for_create_new_user_to_check_response_code"""
    api_status_code = api_resp_codes[req_07_key]
    web_status_code = web_resp_codes[req_07_key]
    assert api_status_code == web_status_code

def test_compare_for_new_user_name_attribute():
    """test_compare_for_new_user_name_attribute"""
    target_attribute = 'name'
    api_response_body = api_resp_bodies[req_07_key]
    web_response_body = web_resp_bodies[req_07_key]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]

def test_compare_for_new_user_job_attribute():
    """test_compare_for_new_user_job_attribute"""
    target_attribute = 'job'
    api_response_body = api_resp_bodies[req_07_key]
    web_response_body = web_resp_bodies[req_07_key]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]


# REQUEST_08: UPDATE

def test_compare_for_put_update_user_to_check_response_code():
    """test_compare_for_put_update_user_to_check_response_code"""
    api_status_code = api_resp_codes[req_08_key]
    web_status_code = web_resp_codes[req_08_key]
    assert api_status_code == web_status_code

def test_compare_for_put_update_user_name_attribute():
    """test_compare_for_put_update_user_name_attribute"""
    target_attribute = 'name'
    api_response_body = api_resp_bodies[req_08_key]
    web_response_body = web_resp_bodies[req_08_key]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]

def test_compare_for_put_update_user_job_attribute():
    """test_compare_for_put_update_user_job_attribute"""
    target_attribute = 'job'
    api_response_body = api_resp_bodies[req_08_key]
    web_response_body = web_resp_bodies[req_08_key]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]


# REQUEST_09: UPDATE

def test_compare_for_patch_update_user_to_check_response_code():
    """test_compare_for_patch_update_user_to_check_response_code"""
    api_status_code = api_resp_codes[req_09_key]
    web_status_code = web_resp_codes[req_09_key]
    assert api_status_code == web_status_code

def test_compare_for_patch_update_user_name_attribute():
    """test_compare_for_patch_update_user_name_attribute"""
    target_attribute = 'name'
    api_response_body = api_resp_bodies[req_09_key]
    web_response_body = web_resp_bodies[req_09_key]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]

def test_compare_for_patch_update_user_job_attribute():
    """test_compare_for_patch_update_user_job_attribute"""
    target_attribute = 'job'
    api_response_body = api_resp_bodies[req_09_key]
    web_response_body = web_resp_bodies[req_09_key]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]


# REQUEST_10: DELETE

def test_compare_for_delete_user_by_id_to_check_response_code():
    """test_compare_for_delete_user_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[req_10_key]
    web_status_code = web_resp_codes[req_10_key]
    assert api_status_code == web_status_code


# REQUEST_11: REGISTER SUCCESSFUL

def test_compare_for_successful_register_to_check_response_code():
    """test_compare_for_successful_register_to_check_response_code"""
    api_status_code = api_resp_codes[req_11_key]
    web_status_code = web_resp_codes[req_11_key]
    assert api_status_code == web_status_code

def test_compare_for_successful_register_to_check_response_body():
    """test_compare_for_successful_register_to_check_response_body"""
    api_response_body = api_resp_bodies[req_11_key]
    web_response_body = web_resp_bodies[req_11_key]
    assert api_response_body == web_response_body


# REQUEST_12: REGISTER UNSUCCESSFUL

def test_compare_for_unsuccessful_register_to_check_response_code():
    """test_compare_for_unsuccessful_register_to_check_response_code"""
    api_status_code = api_resp_codes[req_12_key]
    web_status_code = web_resp_codes[req_12_key]
    assert api_status_code == web_status_code

def test_compare_for_unsuccessful_register_to_check_response_body():
    """test_compare_for_unsuccessful_register_to_check_response_body"""
    api_response_body = api_resp_bodies[req_12_key]
    web_response_body = web_resp_bodies[req_12_key]
    assert api_response_body == web_response_body


# REQUEST_13: LOGIN SUCCESSFUL

def test_compare_for_successful_login_to_check_response_code():
    """test_compare_for_successful_login_to_check_response_code"""
    api_status_code = api_resp_codes[req_13_key]
    web_status_code = web_resp_codes[req_13_key]
    assert api_status_code == web_status_code

def test_compare_for_successful_login_to_check_response_body():
    """test_compare_for_successful_login_to_check_response_body"""
    api_response_body = api_resp_bodies[req_13_key]
    web_response_body = web_resp_bodies[req_13_key]
    assert api_response_body == web_response_body


# REQUEST_14: LOGIN UNSUCCESSFUL

def test_compare_for_unsuccessful_login_to_check_response_code():
    """test_compare_for_unsuccessful_login_to_check_response_code"""
    api_status_code = api_resp_codes[req_14_key]
    web_status_code = web_resp_codes[req_14_key]
    assert api_status_code == web_status_code

def test_compare_for_unsuccessful_login_to_check_response_body():
    """test_compare_for_unsuccessful_login_to_check_response_body"""
    api_response_body = api_resp_bodies[req_14_key]
    web_response_body = web_resp_bodies[req_14_key]
    assert api_response_body == web_response_body


# REQUEST_15: DELAYED RESPONSE

def test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_code():
    """test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_code"""
    api_status_code = api_resp_codes[req_15_key]
    web_status_code = web_resp_codes[req_15_key]
    assert api_status_code == web_status_code

def test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_body():
    """test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_body"""
    api_response_body = api_resp_bodies[req_15_key]
    web_response_body = web_resp_bodies[req_15_key]
    assert api_response_body == web_response_body
