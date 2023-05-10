""" reqres_json_objects.py: This module contains constant JSON objects request/response bodies for REQRES API. """

import json
import datasets.reqres_common_data as reqres


# JSON Objects of Request Bodies for REQRES API

JSON_BODY_REQUEST_CREATE = json.loads(reqres.API_V0_CREATE_REQUEST_BODY)
JSON_BODY_REQUEST_UPDATE_PUT = json.loads(reqres.API_V0_UPDATE_PUT_REQUEST_BODY)
JSON_BODY_REQUEST_UPDATE_PATCH = json.loads(reqres.API_V0_UPDATE_PATCH_REQUEST_BODY)
JSON_BODY_REQUEST_REGISTER_SUCCESSFUL = json.loads(reqres.API_V0_REGISTER_SUCCESSFUL_REQUEST_BODY)
JSON_BODY_REQUEST_REGISTER_UNSUCCESSFUL = json.loads(reqres.API_V0_REGISTER_UNSUCCESSFUL_REQUEST_BODY)
JSON_BODY_REQUEST_LOGIN_SUCCESSFUL = json.loads(reqres.API_V0_LOGIN_SUCCESSFUL_REQUEST_BODY)
JSON_BODY_REQUEST_LOGIN_UNSUCCESSFUL = json.loads(reqres.API_V0_LOGIN_UNSUCCESSFUL_REQUEST_BODY)


# JSON Objects of Response Bodies for REQRES API

JSON_BODY_RESPONSE_LIST_USERS = json.loads(reqres.API_V0_LIST_USERS_RESPONSE_BODY)
JSON_BODY_RESPONSE_SINGLE_USER = json.loads(reqres.API_V0_SINGLE_USER_RESPONSE_BODY)
JSON_BODY_RESPONSE_SINGLE_USER_NOT_FOUND = json.loads(reqres.API_V0_SINGLE_USER_NOT_FOUND_RESPONSE_BODY)
JSON_BODY_RESPONSE_LIST_RESOURCE = json.loads(reqres.API_V0_LIST_RESOURCE_RESPONSE_BODY)
JSON_BODY_RESPONSE_SINGLE_RESOURCE = json.loads(reqres.API_V0_SINGLE_RESOURCE_RESPONSE_BODY)
JSON_BODY_RESPONSE_SINGLE_RESOURCE_NOT_FOUND = json.loads(reqres.API_V0_SINGLE_RESOURCE_NOT_FOUND_RESPONSE_BODY)
JSON_BODY_RESPONSE_CREATE = json.loads(reqres.API_V0_CREATE_RESPONSE_BODY)
JSON_BODY_RESPONSE_UPDATE_PUT = json.loads(reqres.API_V0_UPDATE_PUT_RESPONSE_BODY)
JSON_BODY_RESPONSE_UPDATE_PATCH = json.loads(reqres.API_V0_UPDATE_PATCH_RESPONSE_BODY)
JSON_BODY_RESPONSE_REGISTER_SUCCESSFUL = json.loads(reqres.API_V0_REGISTER_SUCCESSFUL_RESPONSE_BODY)
JSON_BODY_RESPONSE_REGISTER_UNSUCCESSFUL = json.loads(reqres.API_V0_REGISTER_UNSUCCESSFUL_RESPONSE_BODY)
JSON_BODY_RESPONSE_LOGIN_SUCCESSFUL = json.loads(reqres.API_V0_LOGIN_SUCCESSFUL_RESPONSE_BODY)
JSON_BODY_RESPONSE_LOGIN_UNSUCCESSFUL = json.loads(reqres.API_V0_LOGIN_UNSUCCESSFUL_RESPONSE_BODY)
JSON_BODY_RESPONSE_DELAYED = json.loads(reqres.API_V0_DELAYED_RESPONSE_BODY)
