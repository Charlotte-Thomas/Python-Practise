import pytest
# from E_p58 import get_country_index
target = __import__("B1_p58")
get_country_index = target.get_country_index


def test_country_index():
    assert get_country_index('Australia') == 2
    assert get_country_index('usa') == 1
    assert get_country_index('FRANCE') == 3


def test_country_index_errors():
    with pytest.raises(TypeError):
        get_country_index(0)
    with pytest.raises(Exception):
        get_country_index('not a country')


def test_add_show():
  # test for floats
    assert target.add_show_test_version('Merlin', 3) == ['GOT', 'West World', 'Vikings', 'Merlin', 'Medici', 'Tiger King']
    assert target.add_show_test_version('Ozark', 0) == ['Ozark', 'GOT', 'West World', 'Vikings', 'Medici', 'Tiger King']
    assert target.add_show_test_version('Ozark', 10) == ['GOT', 'West World', 'Vikings', 'Medici', 'Tiger King', 'Ozark']

def test_add_show_erros():
    with pytest.raises(TypeError):
        target.add_show_test_version(10, 'string')
    with pytest.raises(TypeError):
        target.add_show_test_version('string', 'string')
    with pytest.raises(TypeError):
        target.add_show_test_version(10, 10)
