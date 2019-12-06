import pytest
class TestClass:
    def sum(self, num1, num2):
        return num1 + num2

    def test_hello(self):
        x=5
        y=6
        assert x+1 == y , "test failed"

    def test_sum(self):
        t = self.sum(1, 2)
        assert t == 4, "test failed"