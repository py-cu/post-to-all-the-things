import unittest
from core import models


class TestModelOperations(unittest.TestCase):
    def test_password_check_simple(self):
        test_pw = "some_test-password134"
        test_user = models.User(name="Jake")
        test_user.set_password(test_pw)
        self.assertTrue(test_user.check_password(test_pw))



if __name__ == "__main__":
    unittest.main()