# api tests with requests

import json
import pytest
import requests
import api_reqres_v0


# REQUEST_01: LIST USERS

api_response_01 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_LIST_USERS_REQUEST_URL)

def test_get_list_of_users_from_page_to_check_response_code():
    """test_get_list_of_users_from_page_to_check_response_code"""
    actual_response_code = api_response_01.status_code
    expected_response_code = api_reqres_v0.API_V0_LIST_USERS_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_page_to_check_response_body():
    """test_get_list_of_users_from_page_to_check_response_body"""
    actual_response_body = api_response_01.json()
    expected_response_body = json.loads(api_reqres_v0.API_V0_LIST_USERS_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_02: SINGLE USER

api_response_02 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_USER_REQUEST_URL)

def test_get_single_user_by_id_to_check_response_code():
    """test_get_single_user_by_id_to_check_response_code"""
    actual_response_code = api_response_02.status_code
    expected_response_code = api_reqres_v0.API_V0_SINGLE_USER_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_user_by_id_to_check_response_body():
    """test_get_get_single_user_by_id_to_check_response_body"""
    actual_response_body = api_response_02.json()
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_USER_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_03: SINGLE USER NOT FOUND

api_response_03 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_REQUEST_URL)

def test_get_no_existing_single_user_by_id_to_check_response_code():
    """test_get_no_existing_single_user_by_id_to_check_response_code"""
    actual_response_code = api_response_03.status_code
    expected_response_code = api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_user_by_id_to_check_response_body():
    """test_get_no_existing_single_user_by_id_to_check_response_body"""
    actual_response_body = api_response_03.json()
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_04: LIST RESOURCE

def get_list_of_resources():
    pass

api_response_04 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_LIST_RESOURCE_REQUEST_URL)

def test_get_list_of_resources_to_check_response_code():
    """test_get_list_of_resources_to_check_response_code"""
    actual_response_code = api_response_04.status_code
    expected_response_code = api_reqres_v0.API_V0_LIST_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_resources_to_check_response_body():
    """test_get_list_of_resources_to_check_response_body"""
    actual_response_body = api_response_04.json()
    expected_response_body = json.loads(api_reqres_v0.API_V0_LIST_RESOURCE_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_05: SINGLE RESOURCE

api_response_05 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_RESOURCE_REQUEST_URL)

def test_get_single_resource_by_id_to_check_response_code():
    """test_get_single_resource_by_id_to_check_response_code"""
    actual_response_code = api_response_05.status_code
    expected_response_code = api_reqres_v0.API_V0_SINGLE_RESOURCE_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_single_resource_by_id_to_check_response_body():
    """test_get_single_resource_by_id_to_check_response_body"""
    actual_response_body = api_response_05.json()
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_RESOURCE_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# REQUEST_06: SINGLE RESOURCE NOT FOUND

api_response_06 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_REQUEST_URL)

def test_get_no_existing_single_resource_by_id_to_check_response_code():
    """test_get_no_existing_single_resource_by_id_to_check_response_code"""
    actual_response_code = api_response_06.status_code
    expected_response_code = api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_no_existing_single_resource_by_id_to_check_response_body():
    """test_get_no_existing_single_resource_by_id_to_check_response_body"""
    actual_response_body = api_response_06.json()
    expected_response_body = json.loads(api_reqres_v0.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_BODY)
    assert actual_response_body == expected_response_body


# positive
def create_new_user():
    pass

# positive
def put_update_user():
    pass

# positive
def patch_update_user():
    pass

# positive
def delete_user():
    pass

# positive
def successful_register():
    pass

# negative
def unsuccessful_register():
    pass

# positive
def successful_login():
    pass

# negative
def unsuccessful_login():
    pass


# REQUEST_15: DELAYED RESPONSE

api_response_15 = requests.get("https://reqres.in" + api_reqres_v0.API_V0_DELAYED_REQUEST_URL)

def test_get_list_of_users_from_the_page_with_delay_to_check_response_code():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_code"""
    actual_response_code = api_response_15.status_code
    expected_response_code = api_reqres_v0.API_V0_DELAYED_RESPONSE_CODE
    assert actual_response_code == expected_response_code

def test_get_list_of_users_from_the_page_with_delay_to_check_response_body():
    """test_get_list_of_users_from_the_page_with_delay_to_check_response_body"""
    actual_response_body = api_response_15.json()
    expected_response_body = json.loads(api_reqres_v0.API_V0_DELAYED_RESPONSE_BODY)
    assert actual_response_body == expected_response_body
