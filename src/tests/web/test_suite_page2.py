""" test_suite_page2.py: This module contains fake tests for false REQRES web page - "https://reqres.in/more-examples.html"."""

import pytest
import datasets.reqres_base_keys as api_keys
import datasets.reqres_common_data as reqres
import datasets.reqres_web_elements as page
import output


# 1) Configuring Selenium Web Driver for Chrome.

print("\nConfiguring Selenium Web Driver ...\n")
# Locate code for configuring a web driver here ...


# 2) Loading REQRES web page.

print("Web Page loading ...")
webpage = reqres.WEBSITE_URL + page.web_pages['page2']
# Locate code for loading a web page here ...

# Let's imagine that this false web page uses fake REQRES API version 2.
api_v2_urls = reqres.get_sample_requests_urls(reqres.AVAILABLE_API_VERSIONS['v2'])


def setup_module(module):
    print("SETUP: ", module)

def teardown_module(module):
    print("TEARDOWN: ", module)


class TestSuite_WebPage2:
    """ TestSuite_WebPage2: This class contains fake tests for false web page - "https://reqres.in/more-examples.html". """

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

    @pytest.mark.parametrize("fake_request_title, fake_request_url, fake_status_code",
        [
            (reqres.REQUEST_TITLE_LIST_USERS, api_v2_urls[api_keys.LIST_USERS], reqres.STATUS_CODE_LIST_USERS),
            (reqres.REQUEST_TITLE_SINGLE_USER, api_v2_urls[api_keys.SINGLE_USER], reqres.STATUS_CODE_SINGLE_USER),
            (reqres.REQUEST_TITLE_SINGLE_USER_NOT_FOUND, api_v2_urls[api_keys.SINGLE_USER_NOT_FOUND], reqres.STATUS_CODE_SINGLE_USER_NOT_FOUND),
            (reqres.REQUEST_TITLE_LIST_RESOURCE, api_v2_urls[api_keys.LIST_RESOURCE], reqres.STATUS_CODE_LIST_RESOURCE),
            (reqres.REQUEST_TITLE_SINGLE_RESOURCE, api_v2_urls[api_keys.SINGLE_RESOURCE], reqres.STATUS_CODE_SINGLE_RESOURCE),
            (reqres.REQUEST_TITLE_SINGLE_RESOURCE_NOT_FOUND, api_v2_urls[api_keys.SINGLE_RESOURCE_NOT_FOUND], reqres.STATUS_CODE_SINGLE_RESOURCE_NOT_FOUND),
            (reqres.REQUEST_TITLE_CREATE, api_v2_urls[api_keys.CREATE], reqres.STATUS_CODE_CREATE),
            (reqres.REQUEST_TITLE_UPDATE_PUT, api_v2_urls[api_keys.UPDATE_PUT], reqres.STATUS_CODE_UPDATE_PUT),
            (reqres.REQUEST_TITLE_UPDATE_PATCH, api_v2_urls[api_keys.UPDATE_PATCH], reqres.STATUS_CODE_UPDATE_PATCH),
            (reqres.REQUEST_TITLE_DELETE, api_v2_urls[api_keys.DELETE], reqres.STATUS_CODE_DELETE),
            (reqres.REQUEST_TITLE_REGISTER_SUCCESSFUL, api_v2_urls[api_keys.REGISTER_SUCCESSFUL], reqres.STATUS_CODE_REGISTER_SUCCESSFUL),
            (reqres.REQUEST_TITLE_REGISTER_UNSUCCESSFUL, api_v2_urls[api_keys.REGISTER_UNSUCCESSFUL], reqres.STATUS_CODE_REGISTER_UNSUCCESSFUL),
            (reqres.REQUEST_TITLE_LOGIN_SUCCESSFUL, api_v2_urls[api_keys.LOGIN_SUCCESSFUL], reqres.STATUS_CODE_LOGIN_SUCCESSFUL),
            (reqres.REQUEST_TITLE_LOGIN_UNSUCCESSFUL, api_v2_urls[api_keys.LOGIN_UNSUCCESSFUL], reqres.STATUS_CODE_LOGIN_UNSUCCESSFUL),
            (reqres.REQUEST_TITLE_DELAYED_RESPONSE, api_v2_urls[api_keys.DELAYED_RESPONSE], reqres.STATUS_CODE_DELAYED_RESPONSE)
        ]
    )
    def test_response_status_code(self , fake_request_title, fake_request_url, fake_status_code):
        """test_response_status_code"""
        output.print_fake_testcase_details(__doc__, fake_request_title, fake_request_url, fake_status_code)
        pass


    @pytest.mark.parametrize("fake_request_title, fake_request_url, fake_response_body",
        [
            (reqres.REQUEST_TITLE_LIST_USERS, api_v2_urls[api_keys.LIST_USERS], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_SINGLE_USER, api_v2_urls[api_keys.SINGLE_USER], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_SINGLE_USER_NOT_FOUND, api_v2_urls[api_keys.SINGLE_USER_NOT_FOUND], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_LIST_RESOURCE, api_v2_urls[api_keys.LIST_RESOURCE], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_SINGLE_RESOURCE, api_v2_urls[api_keys.SINGLE_RESOURCE], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_SINGLE_RESOURCE_NOT_FOUND, api_v2_urls[api_keys.SINGLE_RESOURCE_NOT_FOUND], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_CREATE, api_v2_urls[api_keys.CREATE], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_UPDATE_PUT, api_v2_urls[api_keys.UPDATE_PUT], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_UPDATE_PATCH, api_v2_urls[api_keys.UPDATE_PATCH], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_DELETE, api_v2_urls[api_keys.DELETE], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_REGISTER_SUCCESSFUL, api_v2_urls[api_keys.REGISTER_SUCCESSFUL], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_REGISTER_UNSUCCESSFUL, api_v2_urls[api_keys.REGISTER_UNSUCCESSFUL], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_LOGIN_SUCCESSFUL, api_v2_urls[api_keys.LOGIN_SUCCESSFUL], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_LOGIN_UNSUCCESSFUL, api_v2_urls[api_keys.LOGIN_UNSUCCESSFUL], reqres.FAKE_RESPONSE_BODY_V2),
            (reqres.REQUEST_TITLE_DELAYED_RESPONSE, api_v2_urls[api_keys.DELAYED_RESPONSE], reqres.FAKE_RESPONSE_BODY_V2)
        ]
    )
    def test_response_body_object(self, fake_request_title, fake_request_url, fake_response_body):
        """test_response_body_object"""
        output.print_fake_testcase_details(__doc__, fake_request_title, fake_request_url, fake_response_body)
        pass
