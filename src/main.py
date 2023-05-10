print("\nWelcome to Python Demo Automation for REQRES API !!!\n")

reqres_website_address = "https://reqres.in/"

""" Comment for REQRES API Versions:
Version 1: 'api' - this is the current API identifier from REQRES API developers.
Version 2: 'apiv2' - this is a fake API identifier for the version 2 of REQRES API.
Version 3: 'apiv3' - this is a fake API identifier for the version 3 of REQRES API.
Versions 2 and 3 are false API versions created by me in demonstration aims.
These will be used to demonstrate scaling of API testing in this project.
"""
api_versions = {'v1': 'api', 'v2': 'apiv2', 'v3': 'apiv3'}

""" Comment for REQRES Web Pages:
Page 1: This is a web page returned from REQRES web server when processing default URL ("https://reqres.in/").
Page 2: This is a fake web page returned when processing a fake URL ("https://reqres.in/more-examples.html").
Page 3: This is a fake web page returned from REQRES web server when processing default URL ("https://reqres.in/all-examples.html").
Pages 2 and 3 are false web pages created by me in demonstration aims.
These will be used to demonstrate scaling of web testing in this project.
"""
web_pages = {'page1': '', 'page2': 'more-examples.html', 'page3': 'all-examples.html'}

