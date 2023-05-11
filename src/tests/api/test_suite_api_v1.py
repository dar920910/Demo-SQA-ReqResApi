# test_suite_api_v1.py

import pytest
import requests
import datasets.reqres_base_keys as api_keys
import datasets.reqres_common_data as reqres
import datasets.reqres_json_objects as api_json


# Get the List of Requests' URLs for REQRES API version 1.
api_v1_urls = reqres.get_sample_requests_urls(reqres.AVAILABLE_API_VERSIONS['v1'])

# Get the List of Responses for REQRES API version 1.

api_response_01 = requests.get(api_v1_urls[api_keys.LIST_USERS])
api_response_02 = requests.get(api_v1_urls[api_keys.SINGLE_USER])
api_response_03 = requests.get(api_v1_urls[api_keys.SINGLE_USER_NOT_FOUND])
api_response_04 = requests.get(api_v1_urls[api_keys.LIST_RESOURCE])
api_response_05 = requests.get(api_v1_urls[api_keys.SINGLE_RESOURCE])
api_response_06 = requests.get(api_v1_urls[api_keys.SINGLE_RESOURCE_NOT_FOUND])
api_response_07 = requests.post(api_v1_urls[api_keys.CREATE], api_json.JSON_BODY_REQUEST_CREATE)
api_response_08 = requests.put(api_v1_urls[api_keys.UPDATE_PUT], api_json.JSON_BODY_REQUEST_UPDATE_PUT)
api_response_09 = requests.patch(api_v1_urls[api_keys.UPDATE_PATCH], api_json.JSON_BODY_REQUEST_UPDATE_PATCH)
api_response_10 = requests.delete(api_v1_urls[api_keys.DELETE])
api_response_11 = requests.post(api_v1_urls[api_keys.REGISTER_SUCCESSFUL], api_json.JSON_BODY_REQUEST_REGISTER_SUCCESSFUL)
api_response_12 = requests.post(api_v1_urls[api_keys.REGISTER_UNSUCCESSFUL], api_json.JSON_BODY_REQUEST_REGISTER_UNSUCCESSFUL)
api_response_13 = requests.post(api_v1_urls[api_keys.LOGIN_SUCCESSFUL], api_json.JSON_BODY_REQUEST_LOGIN_SUCCESSFUL)
api_response_14 = requests.post(api_v1_urls[api_keys.LOGIN_UNSUCCESSFUL], api_json.JSON_BODY_REQUEST_LOGIN_UNSUCCESSFUL)
api_response_15 = requests.get(api_v1_urls[api_keys.DELAYED_RESPONSE])


# Define dictionaries to save results of requests (for comparing results of API and WEB tests)

api_tests_response_codes = {}
api_tests_response_codes[api_keys.LIST_USERS] = api_response_01.status_code
api_tests_response_codes[api_keys.SINGLE_USER] = api_response_02.status_code
api_tests_response_codes[api_keys.SINGLE_USER_NOT_FOUND] = api_response_03.status_code
api_tests_response_codes[api_keys.LIST_RESOURCE] = api_response_04.status_code
api_tests_response_codes[api_keys.SINGLE_RESOURCE] = api_response_05.status_code
api_tests_response_codes[api_keys.SINGLE_RESOURCE_NOT_FOUND] = api_response_06.status_code
api_tests_response_codes[api_keys.CREATE] = api_response_07.status_code
api_tests_response_codes[api_keys.UPDATE_PUT] = api_response_08.status_code
api_tests_response_codes[api_keys.UPDATE_PATCH] = api_response_09.status_code
api_tests_response_codes[api_keys.DELETE] = api_response_10.status_code
api_tests_response_codes[api_keys.REGISTER_SUCCESSFUL] = api_response_11.status_code
api_tests_response_codes[api_keys.REGISTER_UNSUCCESSFUL] = api_response_12.status_code
api_tests_response_codes[api_keys.LOGIN_SUCCESSFUL] = api_response_13.status_code
api_tests_response_codes[api_keys.LOGIN_UNSUCCESSFUL] = api_response_14.status_code
api_tests_response_codes[api_keys.DELAYED_RESPONSE] = api_response_15.status_code

api_tests_response_bodies = {}
api_tests_response_bodies[api_keys.LIST_USERS] = api_response_01.json()
api_tests_response_bodies[api_keys.SINGLE_USER] = api_response_02.json()
api_tests_response_bodies[api_keys.SINGLE_USER_NOT_FOUND] = api_response_03.json()
api_tests_response_bodies[api_keys.LIST_RESOURCE] = api_response_04.json()
api_tests_response_bodies[api_keys.SINGLE_RESOURCE] = api_response_05.json()
api_tests_response_bodies[api_keys.SINGLE_RESOURCE_NOT_FOUND] = api_response_06.json()
api_tests_response_bodies[api_keys.CREATE] = api_response_07.json()
api_tests_response_bodies[api_keys.UPDATE_PUT] = api_response_08.json()
api_tests_response_bodies[api_keys.UPDATE_PATCH] = api_response_09.json()
api_tests_response_bodies[api_keys.REGISTER_SUCCESSFUL] = api_response_11.json()
api_tests_response_bodies[api_keys.REGISTER_UNSUCCESSFUL] = api_response_12.json()
api_tests_response_bodies[api_keys.LOGIN_SUCCESSFUL] = api_response_13.json()
api_tests_response_bodies[api_keys.LOGIN_UNSUCCESSFUL] = api_response_14.json()
api_tests_response_bodies[api_keys.DELAYED_RESPONSE] = api_response_15.json()



def setup_module(module):
    print("SETUP: ", module)

def teardown_module(module):
    print("TEARDOWN: ", module)


def print_testing_results(actual_result, expected_result):
    print("\nActual Result: {0}\nExpected Result: {1}\n".format(actual_result, expected_result))

def print_testcase_delimiter():
    """print_testcase_delimiter(): Print a line of symbols to separate output for test cases."""

    delimiter_symbol = '-'
    delimiter_length = 50

    x = 0
    delimiter = ""
    
    while x < delimiter_length:
        delimiter += delimiter_symbol
        x += 1

    print('\n', delimiter, '\n')


class TestSuite_APIv1:
    """TestSuite_APIv1: This class contains API tests for REQRES API version 1."""

    @classmethod
    def setup_class(cls):
        print("\nTEST CLASS SETUP:\n{0}: {1}".format(cls.__name__, cls.__doc__))

    @classmethod
    def teardown_class(cls):
        print("\nTEST CLASS TEARDOWN: {0}\n".format(cls.__name__))

    def setup_method(self, method):
        print_testcase_delimiter()
        print("\nSetup Test Method: {0}\n".format(method))

    def teardown_method(self, method):
        print("\nTeardown Test Method: {0}\n".format(method))
        print_testcase_delimiter()


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
    def test_response_status_code(self, actual_status_code, expected_status_code):
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
    def test_response_body_object(self, actual_response_body, expected_response_body):
        """test_response_body_object"""
        print_testing_results(actual_response_body, expected_response_body)
        assert actual_response_body == expected_response_body


    @pytest.mark.parametrize("actual_attr_value, expected_attr_value",
        [
            (api_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_NAME], api_json.JSON_BODY_REQUEST_CREATE[api_json.ATTR_USER_NAME]),
            (api_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_JOB], api_json.JSON_BODY_REQUEST_CREATE[api_json.ATTR_USER_JOB]),

            (api_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_NAME], api_json.JSON_BODY_REQUEST_UPDATE_PUT[api_json.ATTR_USER_NAME]),
            (api_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_JOB], api_json.JSON_BODY_REQUEST_UPDATE_PUT[api_json.ATTR_USER_JOB]),
        
            (api_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_NAME], api_json.JSON_BODY_REQUEST_UPDATE_PATCH[api_json.ATTR_USER_NAME]),
            (api_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_JOB], api_json.JSON_BODY_REQUEST_UPDATE_PATCH[api_json.ATTR_USER_JOB])
        ]
    )
    def test_user_object_attribute_is_equal(self, actual_attr_value, expected_attr_value):
        """test_user_object_attribute_is_equal"""
        print_testing_results(actual_attr_value, expected_attr_value)
        assert actual_attr_value == expected_attr_value


    @pytest.mark.parametrize("datetime_attr_value",
        [
            api_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_CREATED],
            api_tests_response_bodies[api_keys.UPDATE_PUT][api_json.ATTR_USER_UPDATED],
            api_tests_response_bodies[api_keys.UPDATE_PATCH][api_json.ATTR_USER_UPDATED]
        ]
    )
    def test_datetime_attribute_is_not_empty(self, datetime_attr_value):
        """test_datetime_attribute_is_not_empty"""
        assert datetime_attr_value != None


    def test_created_user_id_is_positive_value(self):
        """test_created_user_id_is_positive_value"""
        assert int(api_tests_response_bodies[api_keys.CREATE][api_json.ATTR_USER_ID]) > 0
