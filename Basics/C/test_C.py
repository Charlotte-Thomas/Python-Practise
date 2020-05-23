
import pytest
C1 = __import__("C1_p67")

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


# -------------- Test for exceptions ----------------------

def test_TypeErrors():
    with pytest.raises(TypeError):
        C1.num_vowels(6)
        C1.word_reverse(2)
