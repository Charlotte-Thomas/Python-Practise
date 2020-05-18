
# group tests together with classes
# terminal command: pytest ./Tests/test_classes.py
# MUST prefix your class with ---> Test <--- or pytest will skip it


class TestClass:
    def test_one(self):
        x = "hello"
        assert "h" in x

    def test_two(self):
        x = 'test'
        assert 't' in x
