"""reqres_common_data.py: This module contains definitions of constants for expected results used in test suites."""

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
    urls['LIST_USERS'] = get_api_request_url(api_version, API_DEMO_01_LIST_USERS)
    urls['SINGLE_USER'] = get_api_request_url(api_version, API_DEMO_02_SINGLE_USER)
    urls['SINGLE_USER_NOT_FOUND'] = get_api_request_url(api_version, API_DEMO_03_SINGLE_USER_NOT_FOUND)
    urls['LIST_RESOURCE'] = get_api_request_url(api_version, API_DEMO_04_LIST_RESOURCE)
    urls['SINGLE_RESOURCE'] = get_api_request_url(api_version, API_DEMO_05_SINGLE_RESOURCE)
    urls['SINGLE_RESOURCE_NOT_FOUND'] = get_api_request_url(api_version, API_DEMO_06_SINGLE_RESOURCE_NOT_FOUND)
    urls['CREATE'] = get_api_request_url(api_version, API_DEMO_07_CREATE)
    urls['UPDATE_PUT'] = get_api_request_url(api_version, API_DEMO_08_UPDATE_PUT)
    urls['UPDATE_PATCH'] = get_api_request_url(api_version, API_DEMO_09_UPDATE_PATCH)
    urls['DELETE'] = get_api_request_url(api_version, API_DEMO_10_DELETE)
    urls['REGISTER_SUCCESSFUL'] = get_api_request_url(api_version, API_DEMO_11_REGISTER_SUCCESSFUL)
    urls['REGISTER_UNSUCCESSFUL'] = get_api_request_url(api_version, API_DEMO_12_REGISTER_UNSUCCESSFUL)
    urls['LOGIN_SUCCESSFUL'] = get_api_request_url(api_version, API_DEMO_13_LOGIN_SUCCESSFUL)
    urls['LOGIN_UNSUCCESSFUL'] = get_api_request_url(api_version, API_DEMO_14_LOGIN_UNSUCCESSFUL)
    urls['DELAYED_RESPONSE'] = get_api_request_url(api_version, API_DEMO_15_DELAYED_RESPONSE)
    return urls

API_V0_LIST_USERS_REQUEST_URL = "/api/users?page=2" #1
API_V0_SINGLE_USER_REQUEST_URL = "/api/users/2" #2
API_V0_SINGLE_USER_NOT_FOUND_REQUEST_URL = "/api/users/23" #3
API_V0_LIST_RESOURCE_REQUEST_URL = "/api/unknown" #4
API_V0_SINGLE_RESOURCE_REQUEST_URL = "/api/unknown/2" #5
API_V0_SINGLE_RESOURCE_NOT_FOUND_REQUEST_URL = "/api/unknown/23" #6
API_V0_CREATE_REQUEST_URL = "/api/users" #7
API_V0_UPDATE_PUT_REQUEST_URL = "/api/users/2" #8
API_V0_UPDATE_PATCH_REQUEST_URL = "/api/users/2" #9
API_V0_DELETE_REQUEST_URL = "/api/users/2" #10
API_V0_REGISTER_SUCCESSFUL_REQUEST_URL = "/api/register" #11
API_V0_REGISTER_UNSUCCESSFUL_REQUEST_URL = "/api/register" #12
API_V0_LOGIN_SUCCESSFUL_REQUEST_URL = "/api/login" #13
API_V0_LOGIN_UNSUCCESSFUL_REQUEST_URL = "/api/login" #14
API_V0_DELAYED_REQUEST_URL = "/api/users?delay=3" #15




# Note: Values of *_SENDER_ELEMENT_CSS_SELECTOR constants are values from auto-generated .py-script via Selenium IDE.
# Website https://reqres.in uses React, I estimate detecting CSS by manually in browser's DevTools as a more difficult task than using XPath values to identificate web elements in web tests.
# Probably, these values should be replaced to XPath values for the same web elements for improving code understanding and simplify detecting the elements via browser's DevTools.



# API REQUESTS KEYS - these constansts are used as keys in dictionaries to provide ability simplified comparing actual results of api tests and web tests.

API_V0_LIST_USERS_KEY = "LIST_USERS"
API_V0_SINGLE_USER_KEY = "SINGLE_USER"
API_V0_SINGLE_USER_NOT_FOUND_KEY = "SINGLE_USER_NOT_FOUND"
API_V0_LIST_RESOURCE_KEY = "LIST_RESOURCE"
API_V0_SINGLE_RESOURCE_KEY = "SINGLE_RESOURCE"
API_V0_SINGLE_RESOURCE_NOT_FOUND_KEY = "SINGLE_RESOURCE_NOT_FOUND"
API_V0_CREATE_KEY = "CREATE"
API_V0_UPDATE_PUT_KEY = "UPDATE_PUT"
API_V0_UPDATE_PATCH_KEY = "UPDATE_PATCH"
API_V0_DELETE_KEY = "DELETE"
API_V0_REGISTER_SUCCESSFUL_KEY = "REGISTER_SUCCESSFUL"
API_V0_REGISTER_UNSUCCESSFUL_KEY = "REGISTER_UNSUCCESSFUL"
API_V0_LOGIN_SUCCESSFUL_KEY = "LOGIN_SUCCESSFUL"
API_V0_LOGIN_UNSUCCESSFUL_KEY = "LOGIN_UNSUCCESSFUL"
API_V0_DELAYED_KEY = "DELAYED"


# REQUEST_01: LIST USERS

API_V0_LIST_USERS_REQUEST_TITLE = "Send Request_01: List Users"
API_V0_LIST_USERS_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(1) > a"

API_V0_LIST_USERS_RESPONSE_CODE = 200
API_V0_LIST_USERS_RESPONSE_BODY = """{
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


# REQUEST_02: SINGLE USER

API_V0_SINGLE_USER_REQUEST_TITLE = "Send Request_02: Single User"
API_V0_SINGLE_USER_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(2) > a"

API_V0_SINGLE_USER_RESPONSE_CODE = 200
API_V0_SINGLE_USER_RESPONSE_BODY = """{
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


# REQUEST_03: SINGLE USER NOT FOUND

API_V0_SINGLE_USER_NOT_FOUND_REQUEST_TITLE = "Send Request_03: Single User Not Found"
API_V0_SINGLE_USER_NOT_FOUND_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(3) > a"

API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_CODE = 404
API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_BODY = "{}"


# REQUEST_04: LIST RESOURCE

API_V0_LIST_RESOURCE_REQUEST_TITLE = "Send Request_04: List Resource"
API_V0_LIST_RESOURCE_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(4) > a"

API_V0_LIST_RESOURCE_RESPONSE_CODE = 200
API_V0_LIST_RESOURCE_RESPONSE_BODY = """{
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


# REQUEST_05: SINGLE RESOURCE

API_V0_SINGLE_RESOURCE_REQUEST_TITLE = "Send Request_05: Single Resource"
API_V0_SINGLE_RESOURCE_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(5) > a"

API_V0_SINGLE_RESOURCE_RESPONSE_CODE = 200
API_V0_SINGLE_RESOURCE_RESPONSE_BODY = """{
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


# REQUEST_06: SINGLE RESOURCE NOT FOUND

API_V0_SINGLE_RESOURCE_NOT_FOUND_REQUEST_TITLE = "Send Request_06: Single Resource Not Found"
API_V0_SINGLE_RESOURCE_NOT_FOUND_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(6) > a"

API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_CODE = 404
API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_BODY = "{}"


# REQUEST_07: CREATE

API_V0_CREATE_REQUEST_TITLE = "Send Request_07: Create"
API_V0_CREATE_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(7) > a"

API_V0_CREATE_REQUEST_BODY = """{
    "name": "morpheus",
    "job": "leader"
}
"""
API_V0_CREATE_RESPONSE_CODE = 201
API_V0_CREATE_RESPONSE_BODY = """{
    "name": "morpheus",
    "job": "leader",
    "id": "17",
    "createdAt": "2023-05-08T14:16:23.928Z"
}""" # 'id' and 'createdAt' are not constant values !!!


# REQUEST_08: UPDATE

API_V0_UPDATE_PUT_REQUEST_TITLE = "Send Request_08: Update"
API_V0_UPDATE_PUT_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(8) > a"

API_V0_UPDATE_PUT_REQUEST_BODY = """{
    "name": "morpheus",
    "job": "zion resident"
}
"""
API_V0_UPDATE_PUT_RESPONSE_CODE = 200
API_V0_UPDATE_PUT_RESPONSE_BODY = """{
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2023-05-08T14:23:12.666Z"
}
""" # 'updatedAt' is not a constant value !!!


# REQUEST_09: UPDATE

API_V0_UPDATE_PATCH_REQUEST_TITLE = "Send Request_09: Update"
API_V0_UPDATE_PATCH_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(9) > a"

API_V0_UPDATE_PATCH_REQUEST_BODY = """{
    "name": "morpheus",
    "job": "zion resident"
}
"""
API_V0_UPDATE_PATCH_RESPONSE_CODE = 200
API_V0_UPDATE_PATCH_RESPONSE_BODY = """{
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2023-05-08T14:26:18.555Z"
}
"""


# REQUEST_10: DELETE

API_V0_DELETE_REQUEST_TITLE = "Send Request_10: Delete"
API_V0_DELETE_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(10) > a"

API_V0_DELETE_RESPONSE_CODE = 204


# REQUEST_11: REGISTER SUCCESSFUL

API_V0_REGISTER_SUCCESSFUL_REQUEST_TITLE = "Send Request_11: Register Successful"
API_V0_REGISTER_SUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(11) > a"

API_V0_REGISTER_SUCCESSFUL_REQUEST_BODY = """{
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}"""
API_V0_REGISTER_SUCCESSFUL_RESPONSE_CODE = 200
API_V0_REGISTER_SUCCESSFUL_RESPONSE_BODY = """{
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}"""


# REQUEST_12: REGISTER UNSUCCESSFUL

API_V0_REGISTER_UNSUCCESSFUL_REQUEST_TITLE = "Send Request_12: Register Unsuccessful"
API_V0_REGISTER_UNSUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(12) > a"

API_V0_REGISTER_UNSUCCESSFUL_REQUEST_BODY = """{
    "email": "sydney@fife"
}
"""
API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_CODE = 400
API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_BODY = """{
    "error": "Missing password"
}
"""


# REQUEST_13: LOGIN SUCCESSFUL

API_V0_LOGIN_SUCCESSFUL_REQUEST_TITLE = "Send Request_13: Login Successful"
API_V0_LOGIN_SUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(13) > a"

API_V0_LOGIN_SUCCESSFUL_REQUEST_BODY = """{
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
"""
API_V0_LOGIN_SUCCESSFUL_RESPONSE_CODE = 200
API_V0_LOGIN_SUCCESSFUL_RESPONSE_BODY = """{
    "token": "QpwL5tke4Pnpja7X4"
}"""


# REQUEST_14: LOGIN UNSUCCESSFUL

API_V0_LOGIN_UNSUCCESSFUL_REQUEST_TITLE = "Send Request_14: Login Unsuccessful"
API_V0_LOGIN_UNSUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(14) > a"

API_V0_LOGIN_UNSUCCESSFUL_REQUEST_BODY = """{
    "email": "peter@klaven"
}"""
API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_CODE = 400
API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_BODY = """{
    "error": "Missing password"
}"""


# REQUEST_15: DELAYED RESPONSE

API_V0_DELAYED_REQUEST_TITLE = "Send Request_15: Delayed Response"
API_V0_DELAYED_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(15) > a"

API_V0_DELAYED_RESPONSE_CODE = 200
API_V0_DELAYED_RESPONSE_BODY = """{
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
