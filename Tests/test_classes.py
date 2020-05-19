
# group tests together with classes
# terminal command: pytest ./Tests/test_classes.py OR ✗ pytest -k TestClass (runs specific class)
# MUST prefix your class with ---> Test <--- or pytest will skip it


class TestClass:
    def test_one(self):
        x = "hello"
        assert "p" in x, f"this letter is not in {x}."# allows you to give a specific error message if this is not the case

    def test_two(self):
        x = 'test'
        assert 't' in x

