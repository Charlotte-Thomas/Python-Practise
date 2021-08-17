from inspect import classify_class_attrs
import pytest

from hypothesis import given, strategies as st
from example_exercise.exercises.example import calculate_square_root


@pytest.mark.parametrize(
    "num, error",
    [
        (10, Exception),
        (500, Exception),
        ("a", TypeError),
        ("string", TypeError),
        (674.21, TypeError),
    ],
)
def test_square_root_errors(num, error):
    with pytest.raises(error):
        calculate_square_root(num)


@pytest.mark.parametrize(
    "num, expected",
    [
        (600, 24.49),
        (750, 27.39),
        (1234567, 1111.11),
    ],
)
def test_square_root_returns_correct_results(num, expected):
    assert calculate_square_root(num) == expected


# produces numbers which are over 500
@given(st.integers(min_value=501))
def test_square_root_returns_correct_results_with_random_ints(num):
    assert calculate_square_root(num)


# can also write it like: @given(st.integers().filter(lambda x: x < 500))
@given(st.integers(max_value=500))
def test_square_root_raises_exceptions_with_low_ints(num):
    with pytest.raises(Exception):
        calculate_square_root(num)


@given(st.text())
def test_square_root_raises_error_with_string(string):
    with pytest.raises(TypeError):
        calculate_square_root(string)
