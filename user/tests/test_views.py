from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from django.test.runner import DiscoverRunner as BaseRunner
import time
from django.test import TestCase
from django.urls import reverse
from quiz.models import Score
from minimal_pair.models import MinimalPairCategory


class UserSeleniumTest(StaticLiveServerTestCase):
    """
    Simulates user behavior on website
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(cls):
        """
        Takes user to login form with its data
        """
        cls.selenium.get('%s%s' % (cls.live_server_url, '/login'))
        username_input = cls.selenium.find_element_by_name("username")
        username_input.send_keys('test')
        password_input = cls.selenium.find_element_by_name("password")
        password_input.send_keys('test')
        try:
            time.sleep(1)
            cls.selenium.find_element_by_xpath('//input[@value="Connexion"]')\
                .click()
        except ElementClickInterceptedException:
            login_button = cls.selenium.find_element_by_xpath\
                ('//input[@value="Connexion"]')
            time.sleep(1)
            ActionChains(cls.selenium).move_to_element_with_offset\
                (login_button, 0, -100).click().perform()

    def test_register_form(cls):
        """
        Simulates user registering his account
        """
        cls.selenium.get('%s%s' % (cls.live_server_url, '/register'))
        username_input = cls.selenium.find_element_by_name("username")
        username_input.send_keys('User')
        password_input = cls.selenium.find_element_by_name("password")
        password_input.send_keys('Str0ngP@ssword')
        password_input = cls.selenium.find_element_by_name("password2")
        password_input.send_keys('Str0ngP@ssword')
        try:
            time.sleep(1)
            cls.selenium.find_element_by_xpath('//input[@value="S\'inscrire"]')\
                .click()
        except ElementClickInterceptedException:
            register_button = cls.selenium.find_element_by_xpath\
                ('//input[@value="S\'inscrire"]')
            time.sleep(1)
            ActionChains(cls.selenium).move_to_element_with_offset\
                (register_button, 0, -100).click().perform()


class LoginTest(TestCase):
    """
    Unit tests for User app login
    """

    def test_login_return_expected_html(self):
        """
        Login page is accessible with 'login'
        """
        response = self.client.get(reverse("user:login"))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_valid_credentials(self):
        """
        Login page redirects when right credentials is posted
        """
        response = self.client.post(reverse("user:login"), {
            'username': "test", 'password': "test"
        })
        self.assertTrue(response.status_code, 200)
        self.assertRedirects(response, '/')

    def test_login_invalid_credentials(self):
        """
        Login page does not redirects when wrong
        credentials is posted
        """
        response = self.client.post(reverse("user:login"), {
            'username': "wrong_user", 'password': 'wrong_password'
        })
        self.assertTrue(response.status_code, 200)


class UserRegistrationTest(TestCase):
    """
    Unit tests for User app registration
    """

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
            'username': 'test',
            'password': 'test',
            'password2': 'test',
        }, follow=True, HTTP_X_REQUESTED='XMLHttpRequest')
        self.assertEqual(User.objects.all().count(), 1)


class UserScoreTest(TestCase):
    """
    Unit tests for User app scoring
    """

    def test_redirect_if_not_logged_in(self):
        """
        Not authenticated user is redirect when
        he tries to access score page
        """
        response = self.client.get(reverse('user:user_score_history'))
        self.assertRedirects(response, '/login?next=/user_score_history')
        self.assertEqual(response.status_code, 302)

    def test_view_if_logged_in(self):
        """
        Authenticated user can access his score page
        when logged in
        """
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('user:user_score_history', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request(self):
        """
        Base score chart displayed successfully
        on Ajax request call
        """
        self.client.login(username='test', password='test')
        Score.objects.create(
            score=5
            , user_id=User.objects.first()
            , minimal_pair_category_id=MinimalPairCategory.objects.first()
        )
        self.client.get(reverse('user:user_score_history'))
        response = self.client.post('/score_chart'
                                    , **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request_with_consonant_type(self):
        """
        Consonant score chart displayed successfully
        on Ajax request call
        """
        self.client.login(username='test', password='test')
        self.client.get(reverse('user:user_score_history'
                                ,  kwargs={'type_id': '1'}))
        response = self.client.post('/score_chart/1'
                                    , **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request_with_simple_vowel_subtype(self):
        """
        Simple vowel score chart displayed successfully
        on Ajax request call
        """
        self.client.login(username='test', password='test')
        self.client.get(reverse('user:user_score_history'
                                ,  kwargs={'type_id': '2', 'vowel_type': '6'}))
        response = self.client.post('/score_chart/2/6',
                                    **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request_with_diphthong_subtype(self):
        """
        Diphthong score chart displayed successfully
        on Ajax request call
        """
        self.client.login(username='test', password='test')
        self.client.get(reverse('user:user_score_history',
                                kwargs={'type_id': '2', 'vowel_type': '11'}))
        response = self.client.post('/score_chart/2/11',
                                    **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)


