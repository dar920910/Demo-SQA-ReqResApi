""" main.py: Main module for running tests in an interactive mode."""

def print_welcome_text():
    print("\n*** Welcome to Python Demo Automation for REQRES API !!! ***\n")
    print("\nSelect tests for running via pytest:\n")
    print(" > Print 'demo' to run tests for Web Page 1 and API version 1")
    print(" > Print 'page1' to run tests for Web Page 1 (web tests for REQRES.IN)")
    print(" > Print 'page2' to run tests for Web Page 2 (fake web tests)")
    print(" > Print 'page3' to run tests for Web Page 3 (fake web tests)")
    print(" > Print 'api1' to run tests for API version 1 (API tests for REQRES API)")
    print(" > Print 'api2' to run tests for API version 1 (fake API tests)")
    print(" > Print 'api3' to run tests for API version 1 (fake API tests)")
    print("\n Print 'quit' to exit from the program.\n")

def run_tests(tests_list):
    import pytest
    
    pytest_args = ["-v", "-s"]
    pytest_args.extend(tests_list)
    print("Arguments for pytest: ", pytest_args)
    
    pytest.main(pytest_args)

def main():
    print_welcome_text()

    user_input = ''
    valid_choice = False
    tests_modules = []
    while valid_choice == False:
        user_input = input("\nSelect a test suite for running via pytest::\n> ")

        if user_input == 'demo':
            # Web Page 1 and API version 1
            tests_modules.append("src/tests/api/test_suite_api_v1.py")
            tests_modules.append("src/tests/web/test_suite_page1.py")
            tests_modules.append("src/tests/web/test_suite_page1_vs_api_v1.py")
            valid_choice = True
        elif user_input == 'api1':
            # API version 1
            tests_modules.append("src/tests/api/test_suite_api_v1.py")
            valid_choice = True
        elif user_input == 'api2':
            # API version 2
            tests_modules.append("src/tests/api/test_suite_api_v2.py")
            valid_choice = True
        elif user_input == 'api3':
            # API version 3
            tests_modules.append("src/tests/api/test_suite_api_v3.py")
            valid_choice = True
        elif user_input == 'page1':
            # Web Page 1
            tests_modules.append("src/tests/web/test_suite_page1.py")
            valid_choice = True
        elif user_input == 'page2':
            # Web Page 2
            tests_modules.append("src/tests/web/test_suite_page2.py")
            valid_choice = True
        elif user_input == 'page3':
            # Web Page 3
            tests_modules.append("src/tests/web/test_suite_page3.py")
            valid_choice = True
        elif user_input == 'quit':
            print("Exit from the program")
            return
        else:
            print("ERROR: Invalid input. Repeat your attempt.")

    run_tests(tests_modules)

main()
