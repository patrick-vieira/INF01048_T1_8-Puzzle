from unittest import TestCase

from recursion_limit import RecursionLimit


class Test(TestCase):
    def fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def test_f(self):
        with RecursionLimit(10000):
            a = self.fibonacci(100)
        print("vai até estourar")
