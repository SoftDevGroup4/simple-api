import unittest
import app


class TestApp(unittest.TestCase):

    def test_true_when_x_is_17(self):
        response = app.is_grade(3.7)
        self.assertEqual(response, "1st")

    def test_false_when_x_is_36(self):
        response = app.is_grade(3.3)
        self.assertEqual(response, "2nd")

    def test_true_when_x_is_13219(self):
        response = app.is_grade(2.5)
        self.assertEqual(response, "other")

if __name__ == "__main__":
    unittest.main()
