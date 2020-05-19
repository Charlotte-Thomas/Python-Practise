
# Pytest expects tests to be located in files with names begining with test_ or ending with _test.py.
# Prefix test function names with test_, this is what pytest expects our test functions to be named.

# terminal: pytest  - to run all test files
# pytest practise.py::<function_name> to run a specific function


import pytest

# test_lowercase


def lower_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    print(x.lower())
    return x.lower()

lower_case('LOWER CASE')

# tests for scenarios that WORK
def test_capital_case():
    assert lower_case('LOWER CASE') == 'lower case'

# test for scenarios that should CAUSE ERRORS
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        lower_case(9)


# __________________________________________________________________


# test_addition

def multiply_five(x):
    if not isinstance(x, int):
        raise TypeError('Please provide a number argument')
    return x * 5

multiply_five(6)

def test_multiply_five():
    assert multiply_five(2) == 10

def test_raises_exception_on_non_number_arguments():
    with pytest.raises(TypeError):
        multiply_five('string')
