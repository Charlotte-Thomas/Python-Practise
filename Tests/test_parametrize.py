
import pytest
# pytest Tests/test_parametrize.py::test_add

# test add

def add(x, y):
    return x + y


@pytest.mark.parametrize('x,y,expected', [
    (3, 5, 8),
    ('Hello', ' World', 'Hello World'),
    (5.5, 6.5, 12)
])
def test_add(x, y, expected):
    assert add(x, y) == expected


