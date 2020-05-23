
import pytest
C1 = __import__("C1_p67")

# -------------- num_vowels ----------------------

@pytest.mark.parametrize('name, expected', [
  ('jerry', 1),
  ('ELIZABETH', 4),
  ('Samantha', 3)
])
def test(name, expected):
    assert C1.num_vowels(name) == expected
