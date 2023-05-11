""" main.py: Main module for running tests in an interactive mode."""

def print_welcome_text():
    print("\n*** Welcome to Python Demo Automation for REQRES API !!! ***\n")
    print("\nSelect tests for running via pytest:\n")
    print(" > Press '0' to run tests for Web Page 1 and API version 1")
    print(" > Press '1' to run tests for API version 1 (only API tests)")
    print(" > Press '2' to run tests for Web Page 1 (only web tests)")
    print(" > Press '3' to run all API tests (for all available API versions)")
    print(" > Press '4' to run all WEB tests (for all available web Pages)")
    print(" > Press '5' to run ALL tests (all API versions + all web pages)")

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
        user_input = input("\nInput a digit to run wished suite of auto-tests:\n> ")

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

    run_tests(tests_modules)

main()
