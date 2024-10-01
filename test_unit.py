import unittest
import app


class TestApp(unittest.TestCase):

    def test_true_when_x_is_17(self):
        response = app.is_even(17)
        self.assertEqual(response, "False")

    def test_false_when_x_is_36(self):
        response = app.is_even(36)
        self.assertEqual(response, "True")

    def test_true_when_x_is_13219(self):
        response = app.is_even(13219)
        self.assertEqual(response, "False")

if __name__ == "__main__":
    unittest.main()
