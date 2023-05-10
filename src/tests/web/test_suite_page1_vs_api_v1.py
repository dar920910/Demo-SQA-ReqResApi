# test_suite_page1_vs_api_v1.py

import pytest
import datasets.reqres_base_keys as api_keys
import tests.api.test_suite_api_v1 as test_suite_api_v1
import tests.web.test_suite_page1 as test_suite_page1


# Define aliases of dictionaries keys for using in tests.

api_resp_codes = test_suite_api_v1.api_tests_response_codes
api_resp_bodies = test_suite_api_v1.api_tests_response_bodies
web_resp_codes = test_suite_page1.web_tests_response_codes
web_resp_bodies = test_suite_page1.web_tests_response_bodies



# REQUEST_01: LIST USERS

def test_compare_for_get_list_of_users_from_page_to_check_response_code():
    """test_compare_for_get_list_of_users_from_page_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.LIST_USERS]
    web_status_code = web_resp_codes[api_keys.LIST_USERS]
    assert api_status_code == web_status_code

def test_compare_for_get_list_of_users_from_page_to_check_response_body():
    """test_compare_for_get_list_of_users_from_page_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.LIST_USERS]
    web_response_body = web_resp_bodies[api_keys.LIST_USERS]
    assert api_response_body == web_response_body

# REQUEST_02: SINGLE USER

def test_compare_for_get_single_user_by_id_to_check_response_code():
    """test_compare_for_get_single_user_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.SINGLE_USER]
    web_status_code = web_resp_codes[api_keys.SINGLE_USER]
    assert api_status_code == web_status_code

def test_compare_for_get_single_user_by_id_to_check_response_body():
    """test_compare_for_get_get_single_user_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.SINGLE_USER]
    web_response_body = web_resp_bodies[api_keys.SINGLE_USER]
    assert api_response_body == web_response_body


# REQUEST_03: SINGLE USER NOT FOUND

def test_compare_for_get_no_existing_single_user_by_id_to_check_response_code():
    """test_compare_for_get_no_existing_single_user_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.SINGLE_USER_NOT_FOUND]
    web_status_code = web_resp_codes[api_keys.SINGLE_USER_NOT_FOUND]
    assert api_status_code == web_status_code

def test_compare_for_get_no_existing_single_user_by_id_to_check_response_body():
    """test_compare_for_get_no_existing_single_user_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.SINGLE_USER_NOT_FOUND]
    web_response_body = web_resp_bodies[api_keys.SINGLE_USER_NOT_FOUND]
    assert api_response_body == web_response_body


# REQUEST_04: LIST RESOURCE

def test_compare_for_get_list_of_resources_to_check_response_code():
    """test_compare_for_get_list_of_resources_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.LIST_RESOURCE]
    web_status_code = web_resp_codes[api_keys.LIST_RESOURCE]
    assert api_status_code == web_status_code

def test_compare_for_get_list_of_resources_to_check_response_body():
    """test_compare_for_get_list_of_resources_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.LIST_RESOURCE]
    web_response_body = web_resp_bodies[api_keys.LIST_RESOURCE]
    assert api_response_body == web_response_body


# REQUEST_05: SINGLE RESOURCE

def test_compare_for_get_single_resource_by_id_to_check_response_code():
    """test_compare_for_get_single_resource_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.SINGLE_RESOURCE]
    web_status_code = web_resp_codes[api_keys.SINGLE_RESOURCE]
    assert api_status_code == web_status_code

def test_compare_for_get_single_resource_by_id_to_check_response_body():
    """test_compare_for_get_single_resource_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.SINGLE_RESOURCE]
    web_response_body = web_resp_bodies[api_keys.SINGLE_RESOURCE]
    assert api_response_body == web_response_body


# REQUEST_06: SINGLE RESOURCE NOT FOUND

def test_compare_for_get_no_existing_single_resource_by_id_to_check_response_code():
    """test_compare_for_get_no_existing_single_resource_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    web_status_code = web_resp_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    assert api_status_code == web_status_code

def test_compare_for_get_no_existing_single_resource_by_id_to_check_response_body():
    """test_compare_for_get_no_existing_single_resource_by_id_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    web_response_body = web_resp_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND]
    assert api_response_body == web_response_body


# REQUEST_07: CREATE

def test_compare_for_create_new_user_to_check_response_code():
    """test_compare_for_create_new_user_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.CREATE]
    web_status_code = web_resp_codes[api_keys.CREATE]
    assert api_status_code == web_status_code

def test_compare_for_new_user_name_attribute():
    """test_compare_for_new_user_name_attribute"""
    target_attribute = 'name'
    api_response_body = api_resp_bodies[api_keys.CREATE]
    web_response_body = web_resp_bodies[api_keys.CREATE]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]

def test_compare_for_new_user_job_attribute():
    """test_compare_for_new_user_job_attribute"""
    target_attribute = 'job'
    api_response_body = api_resp_bodies[api_keys.CREATE]
    web_response_body = web_resp_bodies[api_keys.CREATE]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]


# REQUEST_08: UPDATE

def test_compare_for_put_update_user_to_check_response_code():
    """test_compare_for_put_update_user_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.UPDATE_PUT]
    web_status_code = web_resp_codes[api_keys.UPDATE_PUT]
    assert api_status_code == web_status_code

def test_compare_for_put_update_user_name_attribute():
    """test_compare_for_put_update_user_name_attribute"""
    target_attribute = 'name'
    api_response_body = api_resp_bodies[api_keys.UPDATE_PUT]
    web_response_body = web_resp_bodies[api_keys.UPDATE_PUT]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]

def test_compare_for_put_update_user_job_attribute():
    """test_compare_for_put_update_user_job_attribute"""
    target_attribute = 'job'
    api_response_body = api_resp_bodies[api_keys.UPDATE_PUT]
    web_response_body = web_resp_bodies[api_keys.UPDATE_PUT]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]


# REQUEST_09: UPDATE

def test_compare_for_patch_update_user_to_check_response_code():
    """test_compare_for_patch_update_user_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.UPDATE_PATCH]
    web_status_code = web_resp_codes[api_keys.UPDATE_PATCH]
    assert api_status_code == web_status_code

def test_compare_for_patch_update_user_name_attribute():
    """test_compare_for_patch_update_user_name_attribute"""
    target_attribute = 'name'
    api_response_body = api_resp_bodies[api_keys.UPDATE_PATCH]
    web_response_body = web_resp_bodies[api_keys.UPDATE_PATCH]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]

def test_compare_for_patch_update_user_job_attribute():
    """test_compare_for_patch_update_user_job_attribute"""
    target_attribute = 'job'
    api_response_body = api_resp_bodies[api_keys.UPDATE_PATCH]
    web_response_body = web_resp_bodies[api_keys.UPDATE_PATCH]
    assert api_response_body[target_attribute] == web_response_body[target_attribute]


# REQUEST_10: DELETE

def test_compare_for_delete_user_by_id_to_check_response_code():
    """test_compare_for_delete_user_by_id_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.DELETE]
    web_status_code = web_resp_codes[api_keys.DELETE]
    assert api_status_code == web_status_code


# REQUEST_11: REGISTER SUCCESSFUL

def test_compare_for_successful_register_to_check_response_code():
    """test_compare_for_successful_register_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.REGISTER_SUCCESSFUL]
    web_status_code = web_resp_codes[api_keys.REGISTER_SUCCESSFUL]
    assert api_status_code == web_status_code

def test_compare_for_successful_register_to_check_response_body():
    """test_compare_for_successful_register_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.REGISTER_SUCCESSFUL]
    web_response_body = web_resp_bodies[api_keys.REGISTER_SUCCESSFUL]
    assert api_response_body == web_response_body


# REQUEST_12: REGISTER UNSUCCESSFUL

def test_compare_for_unsuccessful_register_to_check_response_code():
    """test_compare_for_unsuccessful_register_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.REGISTER_UNSUCCESSFUL]
    web_status_code = web_resp_codes[api_keys.REGISTER_UNSUCCESSFUL]
    assert api_status_code == web_status_code

def test_compare_for_unsuccessful_register_to_check_response_body():
    """test_compare_for_unsuccessful_register_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.REGISTER_UNSUCCESSFUL]
    web_response_body = web_resp_bodies[api_keys.REGISTER_UNSUCCESSFUL]
    assert api_response_body == web_response_body


# REQUEST_13: LOGIN SUCCESSFUL

def test_compare_for_successful_login_to_check_response_code():
    """test_compare_for_successful_login_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.LOGIN_SUCCESSFUL]
    web_status_code = web_resp_codes[api_keys.LOGIN_SUCCESSFUL]
    assert api_status_code == web_status_code

def test_compare_for_successful_login_to_check_response_body():
    """test_compare_for_successful_login_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.LOGIN_SUCCESSFUL]
    web_response_body = web_resp_bodies[api_keys.LOGIN_SUCCESSFUL]
    assert api_response_body == web_response_body


# REQUEST_14: LOGIN UNSUCCESSFUL

def test_compare_for_unsuccessful_login_to_check_response_code():
    """test_compare_for_unsuccessful_login_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.LOGIN_UNSUCCESSFUL]
    web_status_code = web_resp_codes[api_keys.LOGIN_UNSUCCESSFUL]
    assert api_status_code == web_status_code

def test_compare_for_unsuccessful_login_to_check_response_body():
    """test_compare_for_unsuccessful_login_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.LOGIN_UNSUCCESSFUL]
    web_response_body = web_resp_bodies[api_keys.LOGIN_UNSUCCESSFUL]
    assert api_response_body == web_response_body


# REQUEST_15: DELAYED RESPONSE

def test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_code():
    """test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_code"""
    api_status_code = api_resp_codes[api_keys.DELAYED_RESPONSE]
    web_status_code = web_resp_codes[api_keys.DELAYED_RESPONSE]
    assert api_status_code == web_status_code

def test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_body():
    """test_compare_for_get_list_of_users_from_the_page_with_delay_to_check_response_body"""
    api_response_body = api_resp_bodies[api_keys.DELAYED_RESPONSE]
    web_response_body = web_resp_bodies[api_keys.DELAYED_RESPONSE]
    assert api_response_body == web_response_body
