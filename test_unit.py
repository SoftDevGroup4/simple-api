import unittest
import app


class TestApp(unittest.TestCase):

    def test_x_is_1(self):
        response = app.isodd(1)
        self.assertEqual(response, "True")

    def test_x_is_0(self):
        response = app.isodd(0)
        self.assertEqual(response, "False")

    def test_x_is_neg2(self):
        response = app.isodd(-2)
        self.assertEqual(response, "False")


if __name__ == "__main__":
    unittest.main()
