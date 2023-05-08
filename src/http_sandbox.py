""" http_sandbox.py: This module contains experimental functions to test API requests via HTTP client libs from Python interactive mode. """

import http.client
import requests
import json


def investigate_all_users_request_v1():
    
    target_host = 'reqres.in'
    target_method = 'GET'
    target_url = '/api/users'
    print("\n*** REQUEST via HTTP.CLIENT: {0} {1} [Host: {2}] ***\n".format(target_method, target_url, target_host))
    
    conn = http.client.HTTPSConnection(target_host)
    conn.request(target_method, target_url)
    
    response = conn.getresponse()
    print("1) Status Code: {0} {1}\n".format(response.status, response.reason))

    response_body = response.read()
    print("2) Response Body:\n\n", response_body, '\n')
    print("3) Response Headers:\n\n", response.headers, '\n')


def investigate_all_users_request_v2():
    url = 'https://reqres.in/api/users'
    print("\n*** REQUEST via REQUESTS: ", url, "***\n")
    response = requests.get(url)
    
    print("1) Status Code: {0} {1} [elapsed: {2}s]\n".format(response.status_code, response.reason, response.elapsed.total_seconds()))
    print("2) Response Body:\n\n", response.text, '\n')
    print("3) Response Headers:\n\n", response.headers, '\n')


def investigate_single_user_response_body():

    test_json_object = json.loads("""{
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
    )

    print("\n--> Test JSON object:\n", test_json_object)

    request_url = 'https://reqres.in/api/users/2'
    response = requests.get(request_url)
    response_body_json_object = json.loads(response.text)
    print("\n--> Response body JSON object:\n", response_body_json_object)

    if test_json_object == response_body_json_object:
        print("\nBoth JSON objects are equal.\n")
    else:
        print("\nBoth JSON objects are different.\n")


# EXPERIMENTAL EXECUTION

investigate_all_users_request_v1()
investigate_all_users_request_v2()
investigate_single_user_response_body()
