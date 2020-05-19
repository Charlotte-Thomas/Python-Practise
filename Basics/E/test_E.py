import pytest
from E_p58 import get_country_index


def test_country_index():
    assert get_country_index('Australia') == 2
    assert get_country_index('usa') == 1
    assert get_country_index('FRANCE') == 3


def test_country_index_errors():
    with pytest.raises(TypeError):
        get_country_index(0)
    with pytest.raises(Exception):
        get_country_index('not a country')
