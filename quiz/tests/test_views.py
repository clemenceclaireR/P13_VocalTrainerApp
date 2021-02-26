import time
from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException\
    , NoSuchElementException
from ipa_board.models import SubPhonemeType, PhonemeType, \
    PhonemeInformation
from minimal_pair.models import MinimalPairCategory\
    , MinimalPairInformation
from quiz.models import Score


class QuizTest(TestCase):
    """
    Unit tests for Quiz app
    """

    def test_view_returns_last_page_if_id_page_out_of_range(self):
        """
        View return last page if page number given is out o range
        """
        session = self.client.session
        session['quiz_query'] = []
        session.save()
        response = self.client.get('/quiz/1', {'query': '', 'page': 9}
                                   )
        self.assertEquals(response.context['questions'].number, 1)
        self.assertEqual(response.status_code, 200)

    def test_save_answer(self):
        """
        Answers data is posted successfully
        """
        session = self.client.session
        session['user_answers_list'] = [{'answer': 'king', 'page': '1'}
            , {'answer': 'am', 'page': '2'}
            , {'answer': 'hate', 'page': '3'}
            , {'answer': 'heart', 'page': '4'}
            , {'answer': 'and', 'page': '5'}
            , {'answer': 'hand', 'page': '6'}
            , {'answer': 'arm', 'page': '7'}
            , {'answer': 'arm', 'page': '8'}]
        session.save()
        response = self.client.post('/save_answer', 
                                    {'answer': ['king'], 'page': ['1']})
        self.assertEqual(response.status_code, 200)

    def test_score_returns_expected_html_and_data(self):
        """
        Checks if score page is displayed with the quiz right
        answers and user answers
        """
        session = self.client.session
        session['quiz_query'] = [
            {'id': 74, 'label': 'king', 'ipa_label': '/kɪŋ/'
                , 'associated_sound_id_id': 73, 'category_id_id': 6}
            , {'id': 75, 'label': 'thin', 'ipa_label': '/θɪn/'
                , 'associated_sound_id_id': 76, 'category_id_id': 6}
            , {'id': 76, 'label': 'thing', 'ipa_label': '/θɪŋ/'
                , 'associated_sound_id_id': 75, 'category_id_id': 6}
            , {'id': 77, 'label': 'ran', 'ipa_label': '/ɹæn/'
                , 'associated_sound_id_id': 78, 'category_id_id': 6}
            , {'id': 78, 'label': 'rang', 'ipa_label': '/ɹæŋ/'
                , 'associated_sound_id_id': 77, 'category_id_id': 6}
            , {'id': 82, 'label': 'tongue', 'ipa_label': '/tʌŋ/'
                , 'associated_sound_id_id': 81, 'category_id_id': 6}
            , {'id': 84, 'label': 'bang', 'ipa_label': '/bæŋ/'
                , 'associated_sound_id_id': 83, 'category_id_id': 6}
            , {'id': 86, 'label': 'hanged', 'ipa_label': '/hæŋd/'
                , 'associated_sound_id_id': 85, 'category_id_id': 6}]

        session['score'] = None

        session['user_answers_list'] = [{'answer': 'king', 'page': '1'}
            , {'answer': 'thin', 'page': '2'}, {'answer': 'thing', 'page': '3'}
            , {'answer': 'ran', 'page': '4'}, {'answer': 'rang', 'page': '5'}
            , {'answer': 'tongue', 'page': '6'}
            , {'answer': 'bang', 'page': '7'}, {'answer': 'hand', 'page': '8'}]
        session.save()
        response = self.client.get(reverse("quiz:score", kwargs={'category_id': '1'}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['user_answers_label']), 8)
        self.assertEqual(len(response.context['right_answers_list']), 8)

    def test_save_score(self):
        """
        Check if score is registered
        """
        self.client.login(username='test', password='test')
        session = self.client.session
        session['score'] = 7
        session.save()
        response = self.client.get(reverse('quiz:save_results', kwargs={
            'category_id': '1'}))
        self.assertEqual(Score.objects.all().count(), 1)
        self.assertEqual(response.status_code, 302)


class SeleniumQuizTest(StaticLiveServerTestCase):
    """
    Simulates user using the quiz and registering its score
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("excludeSwitches"
                                        , ["enable-logging"])

        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_quiz_display(cls):
        """
        Renders quiz first page and get user to choose one
        of the available answers
        """

        cls.selenium.get('%s%s' % (cls.live_server_url, '/quiz/1'))

        try:
            cls.selenium.find_element_by_id('first_answer').click()
        except ElementClickInterceptedException:
            play_button = cls.selenium.find_element_by_id('first_answer')
            time.sleep(1)
            ActionChains(cls.selenium).move_to_element_with_offset \
                (play_button, 0, -100).click().perform()
