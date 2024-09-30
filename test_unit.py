import unittest
from app import app


class TestApp(unittest.TestCase):
    
    def true_when_x_is_17(self):
        response = app.get("/is_prime/17")
        self.assertEqual(response.data.decode(), "True")

    def false_when_x_is_36(self):
        response = app.get("/is_prime/36")
        self.assertEqual(response.data.decode(), "True")

    def true_when_x_is_13219(self):
        response = app.get("/is_prime/13219")
        self.assertEqual(response.data.decode(), "True")

    def true_when_x_is_17(self):
        # Test for invalid input
        response = app.get("/is_prime/a")
        self.assertEqual(response.json, {"error_msg": "inputs must be numbers"})


if __name__ == "__main__a":
    unittest.main()
