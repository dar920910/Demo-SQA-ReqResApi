# test_suite_page1_vs_api_v1.py

import pytest
import datasets.reqres_base_keys as api_keys
import datasets.reqres_json_objects as api_json
import tests.api.test_suite_api_v1 as api_res
import tests.web.test_suite_page1 as web_res


def setup_function(function):
    print("Setup - Test Case: ", function.__doc__)
    
def teardown_function(function):
    print("Teardown - Test Case: ", function.__doc__)


@pytest.mark.parametrize("web_status_code, api_status_code",
    [
        (web_res.web_tests_response_codes[api_keys.LIST_USERS], api_res.api_tests_response_codes[api_keys.LIST_USERS]),
        (web_res.web_tests_response_codes[api_keys.SINGLE_USER], api_res.api_tests_response_codes[api_keys.SINGLE_USER]),
        (web_res.web_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND], api_res.api_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND]),
        (web_res.web_tests_response_codes[api_keys.LIST_RESOURCE], api_res.api_tests_response_codes[api_keys.LIST_RESOURCE]),
        (web_res.web_tests_response_codes[api_keys.SINGLE_RESOURCE], api_res.api_tests_response_codes[api_keys.SINGLE_RESOURCE]),
        (web_res.web_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND], api_res.api_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND]),
        (web_res.web_tests_response_codes[api_keys.CREATE], api_res.api_tests_response_codes[api_keys.CREATE]),
        (web_res.web_tests_response_codes[api_keys.UPDATE_PUT], api_res.api_tests_response_codes[api_keys.UPDATE_PUT]),
        (web_res.web_tests_response_codes[api_keys.UPDATE_PATCH], api_res.api_tests_response_codes[api_keys.UPDATE_PATCH]),
        (web_res.web_tests_response_codes[api_keys.DELETE], api_res.api_tests_response_codes[api_keys.DELETE]),
        (web_res.web_tests_response_codes[api_keys.REGISTER_SUCCESSFUL], api_res.api_tests_response_codes[api_keys.REGISTER_SUCCESSFUL]),
        (web_res.web_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL], api_res.api_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL]),
        (web_res.web_tests_response_codes[api_keys.LOGIN_SUCCESSFUL], api_res.api_tests_response_codes[api_keys.LOGIN_SUCCESSFUL]),
        (web_res.web_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL], api_res.api_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL]),
        (web_res.web_tests_response_codes[api_keys.DELAYED_RESPONSE], api_res.api_tests_response_codes[api_keys.DELAYED_RESPONSE])
    ]
)
def test_web_and_api_response_status_codes_are_equal(web_status_code, api_status_code):
    """test_case_web_and_api_response_status_codes_are_equal"""
    assert web_status_code == api_status_code


@pytest.mark.parametrize("web_response_body, api_response_body",
    [
        (web_res.web_tests_response_bodies[api_keys.LIST_USERS], api_res.api_tests_response_bodies[api_keys.LIST_USERS]),
        (web_res.web_tests_response_bodies[api_keys.SINGLE_USER], api_res.api_tests_response_bodies[api_keys.SINGLE_USER]),
        (web_res.web_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND], api_res.api_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND]),
        (web_res.web_tests_response_bodies[api_keys.LIST_RESOURCE], api_res.api_tests_response_bodies[api_keys.LIST_RESOURCE]),
        (web_res.web_tests_response_bodies[api_keys.SINGLE_RESOURCE], api_res.api_tests_response_bodies[api_keys.SINGLE_RESOURCE]),
        (web_res.web_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND], api_res.api_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND]),
        (web_res.web_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL], api_res.api_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL]),
        (web_res.web_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL], api_res.api_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL]),
        (web_res.web_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL], api_res.api_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL]),
        (web_res.web_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL], api_res.api_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL]),
        (web_res.web_tests_response_bodies[api_keys.DELAYED_RESPONSE], api_res.api_tests_response_bodies[api_keys.DELAYED_RESPONSE])
    ]
)
def test_web_and_api_response_bodies_are_equal(web_response_body, api_response_body):
    """test_web_and_api_response_bodies_are_equal"""
    assert web_response_body == api_response_body


@pytest.mark.parametrize("web_obj_attr_value, api_obj_attr_value",
    [
        (web_res.web_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_NAME], api_res.api_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_NAME]),
        (web_res.web_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_JOB], api_res.api_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_JOB]),

        (web_res.web_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_NAME], api_res.api_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_NAME]),
        (web_res.web_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_JOB], api_res.api_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_JOB]),
        
        (web_res.web_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_NAME], api_res.api_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_NAME]),
        (web_res.web_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_JOB], api_res.api_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_JOB])
    ]
)
def test_web_and_api_user_object_attributes_are_equal(web_obj_attr_value, api_obj_attr_value):
    """test_user_object_attribute_is_equal"""
    assert web_obj_attr_value == api_obj_attr_value
