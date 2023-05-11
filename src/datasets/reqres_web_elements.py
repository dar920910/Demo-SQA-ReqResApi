""" reqres_web_elements.py: This module contains definitions of web elements used by Selenium web driver in web tests. """


""" Comment for REQRES Web Pages:
Page 1: This is a web page returned from REQRES web server when processing default URL ("https://reqres.in/").
Page 2: This is a fake web page returned when processing a fake URL ("https://reqres.in/more-examples.html").
Page 3: This is a fake web page returned from REQRES web server when processing default URL ("https://reqres.in/all-examples.html").
Pages 2 and 3 are false web pages created by me in demonstration aims.
These will be used to demonstrate scaling of web testing in this project.
"""
web_pages = {'page1': '', 'page2': 'more-examples.html', 'page3': 'all-examples.html'}


# CSS selectors' constants from a script generated via Selenium IDE.

ELEMENT_CSS_SELECTOR_REQUEST_LIST_USERS = "li:nth-child(1) > a"
ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_USER = "li:nth-child(2) > a"
ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_USER_NOT_FOUND = "li:nth-child(3) > a"
ELEMENT_CSS_SELECTOR_REQUEST_LIST_RESOURCE = "li:nth-child(4) > a"
ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_RESOURCE = "li:nth-child(5) > a"
ELEMENT_CSS_SELECTOR_REQUEST_SINGLE_RESOURCE_NOT_FOUND = "li:nth-child(6) > a"
ELEMENT_CSS_SELECTOR_REQUEST_CREATE = "li:nth-child(7) > a"
ELEMENT_CSS_SELECTOR_REQUEST_UPDATE_PUT = "li:nth-child(8) > a"
ELEMENT_CSS_SELECTOR_REQUEST_UPDATE_PATCH = "li:nth-child(9) > a"
ELEMENT_CSS_SELECTOR_REQUEST_DELETE = "li:nth-child(10) > a"
ELEMENT_CSS_SELECTOR_REQUEST_REGISTER_SUCCESSFUL = "li:nth-child(11) > a"
ELEMENT_CSS_SELECTOR_REQUEST_REGISTER_UNSUCCESSFUL = "li:nth-child(12) > a"
ELEMENT_CSS_SELECTOR_REQUEST_LOGIN_SUCCESSFUL = "li:nth-child(13) > a"
ELEMENT_CSS_SELECTOR_REQUEST_LOGIN_UNSUCCESSFUL = "li:nth-child(14) > a"
ELEMENT_CSS_SELECTOR_REQUEST_DELAYED_RESPONSE = "li:nth-child(15) > a"

ELEMENT_CSS_SELECTOR_RESPONSE_CODE = ".response-code"
ELEMENT_CSS_SELECTOR_RESPONSE_BODY = ".response > pre"


# This is a value of time in seconds to wait for updating web elements after sending requests by Selenium web driver.
WAITING_TIMEOUT = 5
