import unittest
from payheropy.core import initiate_payment

class TestCore(unittest.TestCase):
    def test_initiate_payment(self):
        result = initiate_payment("254712345678", 100)
        self.assertEqual(result["status"], "success")
        self.assertIn("initiated", result["message"])
        
if __name__ == "__main__":
    unittest.main()
