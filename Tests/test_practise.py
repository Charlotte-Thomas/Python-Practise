
# Pytest expects tests to be located in files with names begining with test_ or ending with _test.py.
# Prefix test function names with test_, this is what pytest expects our test functions to be named.


# test_lowercase.py
import pytest


def lower_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    print(x.lower())
    return x.lower()

lower_case('LOWER CASE')

def test_capital_case():
    assert lower_case('LOWER CASE') == 'lower case'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        lower_case(9)
