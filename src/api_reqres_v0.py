"""api_reqres_v0.py: This module contains definitions of constants for expected results used in test suites for the default API version (named as v0)."""


# REQUEST_01: LIST USERS

API_V0_LIST_USERS_REQUEST_TITLE = "Send Request_01: List Users"
API_V0_LIST_USERS_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(1) > a"
API_V0_LIST_USERS_REQUEST_URL = "/api/users?page=2"
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
API_V0_SINGLE_USER_REQUEST_URL = "/api/users/2"
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
API_V0_SINGLE_USER_NOT_FOUND_REQUEST_URL = "/api/users/23"
API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_CODE = 404
API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_BODY = "{}"


# REQUEST_04: LIST RESOURCE

API_V0_LIST_RESOURCE_REQUEST_TITLE = "Send Request_04: List Resource"
API_V0_LIST_RESOURCE_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(4) > a"
API_V0_LIST_RESOURCE_REQUEST_URL = "/api/unknown"
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
API_V0_SINGLE_RESOURCE_REQUEST_URL = "/api/unknown/2"
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
API_V0_SINGLE_RESOURCE_NOT_FOUND_REQUEST_URL = "/api/unknown/23"
API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_CODE = 404
API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_BODY = "{}"


# REQUEST_07: CREATE

API_V0_CREATE_REQUEST_TITLE = "Send Request_07: Create"
API_V0_CREATE_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(7) > a"
API_V0_CREATE_REQUEST_URL = "/api/users"
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
API_V0_UPDATE_PUT_REQUEST_URL = "/api/users/2"
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
API_V0_UPDATE_PATCH_REQUEST_URL = "/api/users/2"
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
API_V0_DELETE_REQUEST_URL = "/api/users/2"
API_V0_DELETE_RESPONSE_CODE = 204
API_V0_DELETE_RESPONSE_BODY = ""


# REQUEST_11: REGISTER SUCCESSFUL

API_V0_REGISTER_SUCCESSFUL_REQUEST_TITLE = "Send Request_11: Register Successful"
API_V0_REGISTER_SUCCESSFUL_SENDER_ELEMENT_CSS_SELECTOR = "li:nth-child(11) > a"
API_V0_REGISTER_SUCCESSFUL_REQUEST_URL = "/api/register"
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
API_V0_REGISTER_UNSUCCESSFUL_REQUEST_URL = "/api/register"
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
API_V0_LOGIN_SUCCESSFUL_REQUEST_URL = "/api/login"
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
API_V0_LOGIN_UNSUCCESSFUL_REQUEST_URL = "/api/login"
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
API_V0_DELAYED_REQUEST_URL = "/api/users?delay=3"
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
