
import pytest
from array import *
import os # for use of mocker

C1 = __import__("C1_p67")
C2 = __import__("C2_p72")
C3 = __import__("C3_p79")

# -------------- num_vowels ----------------------


@pytest.mark.parametrize('name, expected', [
    ('jerry', 1),
    ('ELIZABETH', 4),
    ('Samantha', 3),
])
def test_vowels(name, expected):
    assert C1.num_vowels(name) == expected

# -------------- word_reversed ----------------------


@pytest.mark.parametrize('word, expected', [
    ('hello', 'olleh'),
    ('BACKWARDS', 'SDRAWKCAB'),
    ('scor-_es', 'se_-rocs')
])
def test_reversed(word, expected):
    assert C1.word_reverse(word) == expected


# -------------- create_array ----------------------

@pytest.mark.parametrize('nums_list, expected', [
    ([11, 12, 13, 14, 15], array('i', [11, 12, 13, 14, 15])),
    ([10, 1, 13, 22, 20], array('i', [10, 13, 20])),
    (['string', 1.6, 17, 13.3, 19], array('i', [17, 19])),
    (['string', 'string', 'string', 'string', 'string'], array('i'))
])
def test_create_array(nums_list, expected):
    assert C2.create_array(nums_list) == expected


# -------------- conjoin_array ----------------------

@pytest.mark.parametrize('nums_list, expected', [
    ([5, 2, 9], [2, 3, 3, 3, 3, 3, 5, 9,]),
    ([100, 1, 4], [1, 3, 3, 3, 3, 3, 4, 100,])
])
def test_conjoin_arrays(monkeypatch, nums_list, expected):
    monkeypatch.setattr('random.randint', lambda a, b: 3) # will override random.randint in conjoin function... a & b for num of arguments in random func.
    assert C2.conjoin_arrays(nums_list) == expected



# -------------- Test for exceptions ----------------------

def test_Errors():
    with pytest.raises(TypeError):
        C1.num_vowels(6)
        C1.word_reverse(2)
        C2.create_array('string')
        C2.conjoin_arrays(['string', 'string', 'string'])
        C2.conjoin_arrays([1.4, 4, 5.6])

    with pytest.raises(Exception):
        C2.create_array('string')
        C2.create_array(1)
        C2.create_array([12, 14, 15, 17, 20, 13])
        C2.conjoin_arrays('string')
        C2.conjoin_arrays(7)
        C2.conjoin_arrays([3, 5])



# -------------- divide_array ----------------------

@pytest.mark.parametrize('num, expected', [
   ('2', [5.28, 10.22, 22.43, 31.73, 49.37]),
   ('4', [2.64, 5.11, 11.22, 15.86, 24.68])
])
def test_divide_array(monkeypatch, num, expected):
    monkeypatch.setattr('builtins.input', lambda x: num)
    assert C2.divide_array() == expected

@pytest.mark.parametrize('num', [
   ('0'),
   ('6'),
   ('5.55678'),
   ('string'),
   (9)
])
def test_divide_array_Errors(monkeypatch, num):
    monkeypatch.setattr('builtins.input', lambda x: num)
    with pytest.raises(Exception):
        C2.divide_array()



# -------------- choose_value ----------------------

@pytest.mark.parametrize('row, col, expected', [
  ('1', '1', 7),
  ('3', '2', 0),
  ('0', '1', 5)
])
def test_choose_value(mocker, row, col, expected):
    mocker.patch('builtins.input', side_effect=[row, col]) # mocker allows us to enter vals for multiple inputs (install & import os for use)
    assert C3.choose_value() == expected

@pytest.mark.parametrize('row, col, error', [
   ('-2', '8', IndexError),
   ('9', '11', IndexError),
   ('5.345', '5.89', ValueError),
   ('string', 'string', ValueError),
])
def test_choose_value_Errors(mocker, row, col, error):
    mocker.patch('builtins.input', side_effect=[row, col])
    with pytest.raises(error):
        C3.choose_value()



# -------------- get_info ----------------------

@pytest.mark.parametrize('name, expected', [
  ('jess', [30, 5]),
  ('GEORGE', [45, 6]),
  ('MaRy', [25, 7])
])
def test_get_info(monkeypatch, name, expected):
    people = [{'name': 'Jess', 'age': 30, 'shoe_size': 5},
              {'name': 'George', 'age': 45, 'shoe_size': 6},
              {'name': 'Mary', 'age': 25, 'shoe_size': 7}]
    monkeypatch.setattr('builtins.input', lambda x: name)
    assert C3.get_info(people) == expected

@pytest.mark.parametrize('people, name, error', [
     ([{'name': 'George', 'age': 45, 'shoe_size': 6},
       {'name': 'Mary', 'age': 25, 'shoe_size': 7}], 'jess', TypeError),
     ({'dict': {'name': 'George', 'age': 45, 'shoe_size': 6},
       'dict2': {'name': 'Mary', 'age': 25, 'shoe_size': 7}}, 'jess', TypeError),
     ([{'wrong': 'George', 'age': 45, 'shoe_size': 6},
       {'name': 'Mary', 'wrong': 25, 'shoe_size': 7},
       {'name': 'Jess', 'age': 30, 'wrong': 5}], 'jess', Exception),
     ([{'name': 'Jess', 'age': 30, 'show_size': 5},
       {'name': 'George', 'age': 45, 'shoe_size': 6},
       ['Mary', 25, 7]], 'jess', Exception),
     ([{'name': 'Jess', 'age': 30, 'shoe_size': 5},
       {'name': 'George', 'age': 45, 'shoe_size': 6},
       {'name': 'Mary', 'age': 25, 'shoe_size': 7}], 'bob', Exception)
])
def test_get_info_Errors(monkeypatch, people, name, error):
    monkeypatch.setattr('builtins.input', lambda x: name)
    with pytest.raises(error):
        C3.choose_value(people)