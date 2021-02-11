from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time
from django.test import TestCase
from django.urls import reverse
from quiz.models import Score
from minimal_pair.models import MinimalPairCategory, MinimalPairInformation
from ipa_board.models import SubPhonemeType, PhonemeType, PhonemeInformation


class SeleniumTest(StaticLiveServerTestCase):
    """
    Simulates user behavior on website
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(cls):
        cls.user = User.objects.create_user(username="test",
                                            password="password"
                                            )

    def test_login(cls):
        """
        Takes user to login form with its data
        """
        cls.selenium.get('%s%s' % (cls.live_server_url, '/login'))
        username_input = cls.selenium.find_element_by_name("username")
        username_input.send_keys('test')
        password_input = cls.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        try:
            time.sleep(1)
            cls.selenium.find_element_by_xpath('//input[@value="Connexion"]').click()
        except ElementClickInterceptedException:
            login_button = cls.selenium.find_element_by_xpath('//input[@value="Connexion"]')
            time.sleep(1)
            ActionChains(cls.selenium).move_to_element_with_offset(login_button, 0, -100).click().perform()

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
            cls.selenium.find_element_by_xpath('//input[@value="S\'inscrire"]').click()
        except ElementClickInterceptedException:
            register_button = cls.selenium.find_element_by_xpath('//input[@value="S\'inscrire"]')
            time.sleep(1)
            ActionChains(cls.selenium).move_to_element_with_offset(register_button, 0, -100).click().perform()


class LoginTest(TestCase):
    """
    Login function test
    """

    def setUp(self):
        self.user = User.objects.create_user(id=1,
                                             username="test",
                                             password="test",
                                             )

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
        Login page does not redirects when right credentials is posted
        """
        response = self.client.post(reverse("user:login"), {
            'username': "wrong_user", 'password': 'wrong_password'
        })
        self.assertTrue(response.status_code, 200)


class UserRegistrationTest(TestCase):
    """
    Registration function tests
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


class UserScoreTest(TestCase):
    """
    Scoring functionalities tests
    """

    def setUp(self):
        self.user = User.objects.create_user(id=1,
                                             username="user1",
                                             password="test",
                                             )
        self.phoneme_type1 = PhonemeType.objects.create(id=1, type_name="Consonnes")
        self.phoneme_type2 = PhonemeType.objects.create(id=2, type_name="Voyelles")

        self.sub_phoneme_type1 = SubPhonemeType.objects.create(id=11
                                                               , subtype_name="Diphtongues"
                                                               , phoneme_type_id=PhonemeType.objects.get(
                id=self.phoneme_type2.id).id)
        self.sub_phoneme_type2 = SubPhonemeType.objects.create(id=6
                                                               , subtype_name="Pré-fermées"
                                                               , phoneme_type_id=PhonemeType.objects.get(
                id=self.phoneme_type2.id).id)
        self.phoneme1 = PhonemeInformation.objects.create(id=1
                                                          , label='eɪ'
                                                          , sound_file_name='eɪ.mp3'
                                                          , sub_phoneme_type_id=SubPhonemeType.objects.get
            (id=self.sub_phoneme_type1.id).id)
        self.phoneme2 = PhonemeInformation.objects.create(id=2
                                                          , label='aɪ'
                                                          , sound_file_name='aɪ.mp3'
                                                          , sub_phoneme_type_id=SubPhonemeType.objects.get
            (id=self.sub_phoneme_type1.id).id)

        self.minimal_pair = MinimalPairCategory.objects.create(id=1
                                                               , phoneme=PhonemeInformation.objects.get(
                id=self.phoneme1.id)
                                                               , associated_phoneme=PhonemeInformation.objects.get(
                id=self.phoneme2.id)
                                                               , sub_phoneme_type_id=SubPhonemeType.objects.get(
                id=self.sub_phoneme_type1.id)
                                                               )

        self.score1 = Score.objects.create(id=1
                                           , score=6
                                           , user_id=User.objects.get(id=self.user.id)
                                           , minimal_pair_category_id=MinimalPairCategory.objects.get(
                id=self.minimal_pair.id)
                                           )

        self.score2 = Score.objects.create(id=2
                                           , score=4
                                           , user_id=User.objects.get(id=self.user.id)
                                           , minimal_pair_category_id=MinimalPairCategory.objects.get(
                id=self.minimal_pair.id)
                                           )
        self.score3 = Score.objects.create(id=3
                                           , score=7
                                           , user_id=User.objects.get(id=self.user.id)
                                           , minimal_pair_category_id=MinimalPairCategory.objects.get(
                id=self.minimal_pair.id)
                                           )

    def test_redirect_if_not_logged_in(self):
        """
        Not authenticated user is redirect when he wants to access score page
        """

        response = self.client.get(reverse('user:user_score_history'))
        self.assertRedirects(response, '/login?next=/user_score_history')

    def test_view_if_logged_in(self):
        """
        User wants to access his score page
        """
        self.client.login(username='user1', password='test')
        response = self.client.get(reverse('user:user_score_history', args=(1,)))
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request(self):
        self.client.login(username='user1', password='test')
        self.client.get(reverse('user:user_score_history'))
        response = self.client.post('/score_chart', **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request_with_base_type(self):
        self.client.login(username='user1', password='test')
        self.client.get(reverse('user:user_score_history', args=(1,)))
        response = self.client.post('/score_chart/1', **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request_with_simple_vowel_subtype(self):
        self.client.login(username='user1', password='test')
        self.client.get(reverse('user:user_score_history', args=(1,)))
        response = self.client.post('/score_chart/2/5', **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_score_ajax_request_with_diphthong_subtype(self):
        self.client.login(username='user1', password='test')
        self.client.get(reverse('user:user_score_history', args=(1,)))
        response = self.client.post('/score_chart/2/11', **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

