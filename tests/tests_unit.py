import unittest

from web import models
from web import forms


class TestModelOperations(unittest.TestCase):

    def test_password_check_simple(self):
        test_pw = "some_test-password134"
        test_user = models.User(name="Jake")
        test_user.set_password(test_pw)
        self.assertTrue(test_user.check_password(test_pw))

    def test_password_check_bad(self):
        test_pw = "some_test-password134"
        test_user = models.User(name="Jake")
        test_user.set_password("NOPE")
        self.assertFalse(test_user.check_password(test_pw))


class TestForms(unittest.TestCase):

    def test_valid_new_message(self):
        form = forms.NewMessageForm(date="04-01-2016 06:30:01", message="Oh hai!")
        self.assertTrue(form.validate(), "Form should be valid")

    def test_invalid_msg_new_message(self):
        form = forms.NewMessageForm(date="04-01-2016 06:30:01", message="")
        self.assertFalse(form.validate(), "Form should be invalid")

if __name__ == "__main__":
    unittest.main()