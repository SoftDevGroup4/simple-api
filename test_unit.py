import unittest
import app


class TestApp(unittest.TestCase):

    def test_getcode(self):
        self.assertEqual(app.getcode(), "Hello, world!")

    def test_plus(self):
        self.assertEqual(app.calculate(5, 6), str(11))
        self.assertEqual(app.calculate(1, 4), str(5))
        self.assertEqual(app.calculate(103, 56), str(159))


if __name__ == "__main__":
    unittest.main()
