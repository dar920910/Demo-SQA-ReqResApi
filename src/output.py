""" output.py: This module contains functions for output of info about test execution. """

def print_testing_results(actual_result, expected_result):
    print("\nActual Result: {0}\nExpected Result: {1}\n".format(actual_result, expected_result))

def print_fake_testcase_details(testcase, fake_request_title, fake_request_url, fake_obj):
    print("\nINFO: Fake test is created to demonstrate scaling test automation project.\n")
    print("TEST CASE EXECUTION: {0}\n", format(testcase))
    print("FAKE REQUEST: {0}\n".format(fake_request_title))
    print("FAKE URL: {0}\n".format(fake_request_url))
    print("FAKE OBJECT: {0}\n".format(fake_obj))

def print_testcase_delimiter():
    """print_testcase_delimiter(): Print a line of symbols to separate output for test cases."""

    delimiter_symbol = '-'
    delimiter_length = 50

    x = 0
    delimiter = ""
    
    while x < delimiter_length:
        delimiter += delimiter_symbol
        x += 1

    print('\n', delimiter, '\n')
