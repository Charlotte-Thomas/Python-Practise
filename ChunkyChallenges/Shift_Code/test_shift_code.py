
import pytest
shift = __import__("Shift_Code")

@pytest.mark.parametrize('decode, msg, num, expected', [
  (False, 'abcd', '3', 'defg'),
  (False, 'wxyz', '5', 'bcde'),
  (False, 'hello world', '1', 'ifmmp xpsme'),
  (False, '\' .,', '25', '\' .,'),
  (True, 'abcd', '10', 'qrst'),
  (True, 'CAPS', '1', 'bzor')
])
def test_shift_code(mocker, decode, msg, num, expected):
    mocker.patch('builtins.input', side_effect=[msg, num])
    assert shift.convert_msg(decode) == expected

@pytest.mark.parametrize('decode, char, num, expected', [
  (False, 'a', 5, 5),
  (False, 'z', 10, 9),
  (True, 'a', 8, 18),
  (True, 'z', 15, 10),
])
def test_find_char(decode, char, num, expected):
    assert shift.find_char(decode, char, num) == expected
