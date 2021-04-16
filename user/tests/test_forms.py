from django.test import TestCase
from user.forms import UserRegistrationForm


class RegisterFormTest(TestCase):
    """
    Form tests for register form
    """
    def setUp(self):
        self.data = {
            'username': 'test2',
            'email': 'test@test.fr',
            'password': 'test',
            'password2': 'test',
            'first_name': 'test',
            'last_name': 'test'
        }

    def test_register_form(self):
        """
        Check if register form is valid
        """
        form = UserRegistrationForm(data=self.data)
        self.assertTrue(form.is_valid())
