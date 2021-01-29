from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time


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






