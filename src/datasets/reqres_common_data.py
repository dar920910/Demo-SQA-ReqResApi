""" reqres_common_data.py: This module contains definitions of constants for expected results used in test suites. """

import datasets.reqres_base_keys as api_keys


WEBSITE_URL = "https://reqres.in"

""" Comment for REQRES API Versions:
Version 1: 'api' - this is the current API identifier from REQRES API developers.
Version 2: 'apiv2' - this is a fake API identifier for the version 2 of REQRES API.
Version 3: 'apiv3' - this is a fake API identifier for the version 3 of REQRES API.
Versions 2 and 3 are false API versions created by me in demonstration aims.
These will be used to demonstrate scaling of API testing in this project.
"""
AVAILABLE_API_VERSIONS = {'v1': 'api', 'v2': 'apiv2', 'v3': 'apiv3'}


# Partial URLs for REQRES API requests

API_URL_REQUEST_LIST_USERS = "users?page="
API_URL_REQUEST_SINGLE_USER = "users/"
API_URL_REQUEST_LIST_RESOURCE = "unknown"
API_URL_REQUEST_SINGLE_RESOURCE = "unknown/"
API_URL_REQUEST_REGISTER = "register"
API_URL_REQUEST_LOGIN = "login"
API_URL_REQUEST_DELAYED_RESPONSE = "users?delay="


# Test Data for REQRES API

LAST_PAGE_NUMBER = 2
VALID_USER_ID = 2
INVALID_USER_ID = 23
VALID_RESOURCE_ID = 2
INVALID_RESOURCE_ID = 23
DELAY_VALUE = 3


# Titles of Sample Requests from REQRES API Website for using as docstrings.

REQUEST_TITLE_LIST_USERS = "Request_01: List Users"
REQUEST_TITLE_SINGLE_USER = "Request_02: Single User"
REQUEST_TITLE_SINGLE_USER_NOT_FOUND = "Request_03: Single User Not Found"
REQUEST_TITLE_LIST_RESOURCE = "Request_04: List Resource"
REQUEST_TITLE_SINGLE_RESOURCE = "Request_05: Single Resource"
REQUEST_TITLE_SINGLE_RESOURCE_NOT_FOUND = "Request_06: Single Resource Not Found"
REQUEST_TITLE_CREATE = "Request_07: Create"
REQUEST_TITLE_UPDATE_PUT = "Request_08: Update"
REQUEST_TITLE_UPDATE_PATCH = "Request_09: Update"
REQUEST_TITLE_DELETE = "Request_10: Delete"
REQUEST_TITLE_REGISTER_SUCCESSFUL = "Request_11: Register Successful"
REQUEST_TITLE_REGISTER_UNSUCCESSFUL = "Request_12: Register Unsuccessful"
REQUEST_TITLE_LOGIN_SUCCESSFUL = "Request_13: Login Successful"
REQUEST_TITLE_LOGIN_UNSUCCESSFUL = "Request_14: Login Unsuccessful"
REQUEST_TITLE_DELAYED_RESPONSE = "Request_15: Delayed Response"


# URLs of Sample Requests from REQRES API Website

API_DEMO_01_LIST_USERS = API_URL_REQUEST_LIST_USERS + str(LAST_PAGE_NUMBER)
API_DEMO_02_SINGLE_USER = API_URL_REQUEST_SINGLE_USER + str(VALID_USER_ID)
API_DEMO_03_SINGLE_USER_NOT_FOUND = API_URL_REQUEST_SINGLE_USER + str(INVALID_USER_ID)
API_DEMO_04_LIST_RESOURCE = API_URL_REQUEST_LIST_RESOURCE
API_DEMO_05_SINGLE_RESOURCE = API_URL_REQUEST_SINGLE_RESOURCE + str(VALID_RESOURCE_ID)
API_DEMO_06_SINGLE_RESOURCE_NOT_FOUND = API_URL_REQUEST_SINGLE_RESOURCE + str(INVALID_RESOURCE_ID)
API_DEMO_07_CREATE = API_URL_REQUEST_SINGLE_USER
API_DEMO_08_UPDATE_PUT = API_URL_REQUEST_SINGLE_USER + str(VALID_USER_ID)
API_DEMO_09_UPDATE_PATCH = API_URL_REQUEST_SINGLE_USER + str(VALID_USER_ID)
API_DEMO_10_DELETE = API_URL_REQUEST_SINGLE_USER + str(VALID_USER_ID)
API_DEMO_11_REGISTER_SUCCESSFUL = API_URL_REQUEST_REGISTER
API_DEMO_12_REGISTER_UNSUCCESSFUL = API_URL_REQUEST_REGISTER
API_DEMO_13_LOGIN_SUCCESSFUL = API_URL_REQUEST_LOGIN
API_DEMO_14_LOGIN_UNSUCCESSFUL = API_URL_REQUEST_LOGIN
API_DEMO_15_DELAYED_RESPONSE = API_URL_REQUEST_DELAYED_RESPONSE + str(DELAY_VALUE)


# Functions for processing URLs of REQRES API

def get_api_request_url(api_version, sample_request):
    """get_api_request_url(): Returns URL of a sample request for the specified version of REQRES API."""
    return "{0}/{1}/{2}".format(WEBSITE_URL, api_version, sample_request)

def get_sample_requests_urls(api_version):
    """get_sample_requests_urls(): Returns the dictionary of all available sample requests' URLs for the specified version of REQRES API."""
    urls = {}
    urls[api_keys.LIST_USERS] = get_api_request_url(api_version, API_DEMO_01_LIST_USERS)
    urls[api_keys.SINGLE_USER] = get_api_request_url(api_version, API_DEMO_02_SINGLE_USER)
    urls[api_keys.SINGLE_USER_NOT_FOUND] = get_api_request_url(api_version, API_DEMO_03_SINGLE_USER_NOT_FOUND)
    urls[api_keys.LIST_RESOURCE] = get_api_request_url(api_version, API_DEMO_04_LIST_RESOURCE)
    urls[api_keys.SINGLE_RESOURCE] = get_api_request_url(api_version, API_DEMO_05_SINGLE_RESOURCE)
    urls[api_keys.SINGLE_RESOURCE_NOT_FOUND] = get_api_request_url(api_version, API_DEMO_06_SINGLE_RESOURCE_NOT_FOUND)
    urls[api_keys.CREATE] = get_api_request_url(api_version, API_DEMO_07_CREATE)
    urls[api_keys.UPDATE_PUT] = get_api_request_url(api_version, API_DEMO_08_UPDATE_PUT)
    urls[api_keys.UPDATE_PATCH] = get_api_request_url(api_version, API_DEMO_09_UPDATE_PATCH)
    urls[api_keys.DELETE] = get_api_request_url(api_version, API_DEMO_10_DELETE)
    urls[api_keys.REGISTER_SUCCESSFUL] = get_api_request_url(api_version, API_DEMO_11_REGISTER_SUCCESSFUL)
    urls[api_keys.REGISTER_UNSUCCESSFUL] = get_api_request_url(api_version, API_DEMO_12_REGISTER_UNSUCCESSFUL)
    urls[api_keys.LOGIN_SUCCESSFUL] = get_api_request_url(api_version, API_DEMO_13_LOGIN_SUCCESSFUL)
    urls[api_keys.LOGIN_UNSUCCESSFUL] = get_api_request_url(api_version, API_DEMO_14_LOGIN_UNSUCCESSFUL)
    urls[api_keys.DELAYED_RESPONSE] = get_api_request_url(api_version, API_DEMO_15_DELAYED_RESPONSE)
    return urls


# Request Bodies of Sample Requests from REQRES API Website

REQUEST_BODY_CREATE = """{
    "name": "morpheus",
    "job": "leader"
}
"""

REQUEST_BODY_UPDATE_PUT = """{
    "name": "morpheus",
    "job": "zion resident"
}
"""

REQUEST_BODY_UPDATE_PATCH = """{
    "name": "morpheus",
    "job": "zion resident"
}
"""

REQUEST_BODY_REGISTER_SUCCESSFUL = """{
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}"""

REQUEST_BODY_REGISTER_UNSUCCESSFUL = """{
    "email": "sydney@fife"
}
"""

REQUEST_BODY_LOGIN_SUCCESSFUL = """{
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
"""

REQUEST_BODY_LOGIN_UNSUCCESSFUL = """{
    "email": "peter@klaven"
}"""


# Response Status Codes of Sample Requests from REQRES API Website

STATUS_CODE_LIST_USERS = 200
STATUS_CODE_SINGLE_USER = 200
STATUS_CODE_SINGLE_USER_NOT_FOUND = 404
STATUS_CODE_LIST_RESOURCE = 200
STATUS_CODE_SINGLE_RESOURCE = 200
STATUS_CODE_SINGLE_RESOURCE_NOT_FOUND = 404
STATUS_CODE_CREATE = 201
STATUS_CODE_UPDATE_PUT = 200
STATUS_CODE_UPDATE_PATCH = 200
STATUS_CODE_DELETE = 204
STATUS_CODE_REGISTER_SUCCESSFUL = 200
STATUS_CODE_REGISTER_UNSUCCESSFUL = 400
STATUS_CODE_LOGIN_SUCCESSFUL = 200
STATUS_CODE_LOGIN_UNSUCCESSFUL = 400
STATUS_CODE_DELAYED_RESPONSE = 200


# Request Bodies of Sample Requests from REQRES API Website

RESPONSE_BODY_LIST_USERS = """{
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}"""

RESPONSE_BODY_SINGLE_USER = """{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}"""

RESPONSE_BODY_SINGLE_USER_NOT_FOUND = "{}"

RESPONSE_BODY_LIST_RESOURCE = """{
    "page": 1,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 1,
            "name": "cerulean",
            "year": 2000,
            "color": "#98B2D1",
            "pantone_value": "15-4020"
        },
        {
            "id": 2,
            "name": "fuchsia rose",
            "year": 2001,
            "color": "#C74375",
            "pantone_value": "17-2031"
        },
        {
            "id": 3,
            "name": "true red",
            "year": 2002,
            "color": "#BF1932",
            "pantone_value": "19-1664"
        },
        {
            "id": 4,
            "name": "aqua sky",
            "year": 2003,
            "color": "#7BC4C4",
            "pantone_value": "14-4811"
        },
        {
            "id": 5,
            "name": "tigerlily",
            "year": 2004,
            "color": "#E2583E",
            "pantone_value": "17-1456"
        },
        {
            "id": 6,
            "name": "blue turquoise",
            "year": 2005,
            "color": "#53B0AE",
            "pantone_value": "15-5217"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
"""

RESPONSE_BODY_SINGLE_RESOURCE = """{
    "data": {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
"""

RESPONSE_BODY_SINGLE_RESOURCE_NOT_FOUND = "{}"

RESPONSE_BODY_REGISTER_SUCCESSFUL = """{
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}"""

RESPONSE_BODY_REGISTER_UNSUCCESSFUL = """{
    "error": "Missing password"
}
"""

RESPONSE_BODY_LOGIN_SUCCESSFUL = """{
    "token": "QpwL5tke4Pnpja7X4"
}"""

RESPONSE_BODY_LOGIN_UNSUCCESSFUL = """{
    "error": "Missing password"
}"""

RESPONSE_BODY_DELAYED = """{
    "page": 1,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 1,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        },
        {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        {
            "id": 3,
            "email": "emma.wong@reqres.in",
            "first_name": "Emma",
            "last_name": "Wong",
            "avatar": "https://reqres.in/img/faces/3-image.jpg"
        },
        {
            "id": 4,
            "email": "eve.holt@reqres.in",
            "first_name": "Eve",
            "last_name": "Holt",
            "avatar": "https://reqres.in/img/faces/4-image.jpg"
        },
        {
            "id": 5,
            "email": "charles.morris@reqres.in",
            "first_name": "Charles",
            "last_name": "Morris",
            "avatar": "https://reqres.in/img/faces/5-image.jpg"
        },
        {
            "id": 6,
            "email": "tracey.ramos@reqres.in",
            "first_name": "Tracey",
            "last_name": "Ramos",
            "avatar": "https://reqres.in/img/faces/6-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}"""


# Fake response body for false REQRES API versions.

FAKE_RESPONSE_BODY_V2 = """{
    "support": {
        "api_version": "apiv2"
        "url": "https://reqres.in/more-examples/#support-heading",
        "text": "This is a fake response body from false REQRES API version 2 !!!"
    }
}"""

FAKE_RESPONSE_BODY_V3 = """{
    "support": {
        "api_version": "apiv3"
        "url": "https://reqres.in/all-examples/#support-heading",
        "text": "This is a fake response body from false REQRES API version 3 !!!"
    }
}"""
