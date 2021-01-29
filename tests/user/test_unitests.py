from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTest(TestCase):
    """
    Login function test
    """

    def setUp(self):
        self.user = User.objects.create_user(username="test",
                                             first_name="test",
                                             password="test",
                                             email="test@test.fr")

    def test_login_return_expected_html(self):
        """
        Login page is accessible with 'login'
        """
        response = self.client.get(reverse("user:login"))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_invalid_credentials(self):
        """
        Login page does not redirects when right credentials is posted
        """
        response = self.client.post(reverse("user:login"), {
            'username': "wrong_user", 'password': 'wrong_password'
        })
        self.assertTrue(response.status_code, 200)


class UserRegistrationTest(TestCase):
    """
    Registration function test
    """

    def setUp(self):
        self.user = User.objects.create_user(id=1,
                                             username="user1",
                                             password="test",
                                             )

    def test_register_psw_do_not_match(self):
        """
        Doesn't add user when password don't match in posted data
        """
        self.client.post(reverse("user:register"), data={
            'username': 'test',
            'password': 'test',
            'password2': 'wrong',
        }, follow=True, HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertEqual(User.objects.all().count(), 1)

    def test_register_username_alrd_registered(self):
        """
        Doesn't add user when entered email in posted data
        is already registered
        """
        self.client.post(reverse("user:register"), data={
            'username': 'user1',
            'password': 'test',
            'password2': 'test',
        }, follow=True, HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertEqual(User.objects.all().count(), 1)

