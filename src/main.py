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

def main():
    print("0 - Web Page 1 and API version 1")
    print("1 - API version 1")
    print("2 - Web Page 1")
    print("3 - All API versions")
    print("4 - All Web Pages")
    print("5 - ALL TESTS")
    

    user_input = ''
    valid_choice = False
    tests_modules = []
    while valid_choice == False:
        print("Select tests to run: ")
        user_input = input()

        if user_input == '0':
            # Web Page 1 and API version 1
            tests_modules.append("src/tests/api/test_suite_api_v1.py")
            tests_modules.append("src/tests/web/test_suite_page1.py")
            tests_modules.append("src/tests/web/test_suite_page1_vs_api_v1.py")
            valid_choice = True
        elif user_input == '1':
            # API version 1
            tests_modules.append("src/tests/api/test_suite_api_v1.py")
            valid_choice = True
        elif user_input == '2':
            # Web Page 1
            tests_modules.append("src/tests/web/test_suite_page1.py")
            valid_choice = True
        elif user_input == '3':
            # All API versions
            tests_modules.append("src/tests/api")
            valid_choice = True
        elif user_input == '4':
            # All Web Pages
            tests_modules.append("src/tests/web")
            valid_choice = True
        elif user_input == '5':
            # ALL TESTS
            tests_modules.append("src/tests/")
            valid_choice = True
        elif user_input == 'q':
            print("Exit from the program")
            return
        else:
            print("ERROR")
        
    print(user_input)
    
    import pytest
    
    pytest_args = ["-v", "-s"]
    pytest_args.extend(tests_modules)
    
    print("Arguments for pytest: ", pytest_args)
    
    pytest.main(pytest_args)

main()
