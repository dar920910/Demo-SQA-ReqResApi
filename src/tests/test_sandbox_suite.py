# test_sandbox_suite.py


import pytest


# xUnit-style fixtures

def setup_module(module):
    print("\n**********\n")
    print("\nIn setup_module()...")

def teardown_module(module):
    print("\nIn teardown_module()...")
    print("\n**********\n")

def setup_function(function):
    print("\nIn setup_function(): '", function.__doc__, "' is started.")

def teardown_function(function):
    print("\nIn teardown_function(): '", function.__doc__, "' is finished.")
    print("\n----------\n")


# pytest fixtures

@pytest.fixture
def my_fixture_1():
    """my test fixture"""
    print("\nThis is 'my_fixture_1'\n")

@pytest.fixture
def my_fixture_2():
    """my test fixture"""
    print("\nThis is 'my_fixture_2'\n")

@pytest.fixture
def my_fixture_3():
    """my test fixture"""
    print("\nThis is 'my_fixture_3'\n")


@pytest.mark.usefixtures('my_fixture_1', 'my_fixture_2', 'my_fixture_3')
def test_case_1():
    """test_case_1"""
    assert "PYTEST".lower() == 'pytest'

@pytest.mark.usefixtures('my_fixture_1', 'my_fixture_2')
def test_case_2():
    """test_case_2"""
    assert "pytest".upper() == 'PYTEST'

@pytest.mark.usefixtures('my_fixture_1')
def test_case_3():
    """test_case_3"""
    assert (100 + 50) == 150

def test_case_4(my_fixture_1, my_fixture_2):
    """test_case_4"""
    assert (150 + 50) == 200

def test_case_5(my_fixture_2, my_fixture_1):
    """test_case_5"""
    assert (200 + 50) == 250
    
    
    
class TestClass_00:

    @classmethod
    def setup_class(cls):
        print("\nIn setup_class()...")

    @classmethod
    def teardown_class(cls):
        print("\nIn teardown_class()...")

    def setup_method(self, method):
        print("\nIn setup_method()...")

    def teardown_method(self, method):
        print("\nIn teardown_method()...")


    def test_case_a(self):
        print("\ntest_case_a()\n")

    def test_case_b(self):
        print("\ntest_case_b()\n")

    def test_case_c(self):
        print("\ntest_case_c()\n")