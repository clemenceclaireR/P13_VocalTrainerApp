import time
from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from ipa_board.models import SubPhonemeType, PhonemeType, \
    PhonemeInformation
from minimal_pair.models import MinimalPairCategory, MinimalPairInformation
from quiz.models import Score


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

    def setUp(self):
        self.phoneme_type_vowel = PhonemeType.objects.create \
            (id=2, type_name="Voyelles")

        self.sub_phoneme_type_diphthong = SubPhonemeType.objects \
            .create(id=11
                    , subtype_name="Diphtongues"
                    , phoneme_type_id=PhonemeType.objects.get(
                id=self.phoneme_type_vowel.id).id)

        self.phoneme1 = PhonemeInformation.objects.create(id=1
                                                          , label='eɪ'
                                                          , sound_file_name='eɪ.mp3'
                                                          , sub_phoneme_type_id=SubPhonemeType.objects.get
            (id=self.sub_phoneme_type_diphthong.id).id)
        self.phoneme2 = PhonemeInformation.objects.create(id=2
                                                          , label='ɛ'
                                                          , sound_file_name='ɛ.mp3'
                                                          , sub_phoneme_type_id=SubPhonemeType.objects.get
            (id=self.sub_phoneme_type_diphthong.id).id)

        self.minimal_pair_category = MinimalPairCategory.objects.create(id=1
                                                                        , phoneme=PhonemeInformation.objects.get(
                id=self.phoneme1.id)
                                                                        ,
                                                                        associated_phoneme=PhonemeInformation.objects.get(
                                                                            id=self.phoneme2.id)
                                                                        ,
                                                                        sub_phoneme_type_id=SubPhonemeType.objects.get(
                                                                            id=self.sub_phoneme_type_diphthong.id)
                                                                        )

        self.minimal_pair_information1 = MinimalPairInformation.objects.create(id=1
                                                                               , label="taste"
                                                                               , ipa_label="/teɪst/"
                                                                               , category_id=MinimalPairCategory.objects
                                                                               .get(id=self.minimal_pair_category.id))

        self.minimal_pair_information2 = MinimalPairInformation.objects.create(id=2
                                                                               , label="test"
                                                                               , ipa_label="/tɛst/"
                                                                               ,
                                                                               associated_sound_id=MinimalPairInformation.objects.get(
                                                                                   id=self.minimal_pair_information1.id)
                                                                               , category_id=MinimalPairCategory.objects
                                                                               .get(id=self.minimal_pair_category.id))

        self.minimal_pair_information3 = MinimalPairInformation.objects.create(id=3
                                                                               , label="main"
                                                                               , ipa_label="/meɪn/"
                                                                               , category_id=MinimalPairCategory.objects
                                                                               .get(id=self.minimal_pair_category.id))

        self.minimal_pair_information4 = MinimalPairInformation.objects.create(id=4
                                                                               , label="men"
                                                                               , ipa_label="/mɛn/"
                                                                               ,
                                                                               associated_sound_id=MinimalPairInformation.objects.get(
                                                                                   id=self.minimal_pair_information3.id)
                                                                               , category_id=MinimalPairCategory.objects
                                                                               .get(id=self.minimal_pair_category.id))

        self.minimal_pair_information1.associated_sound_id = MinimalPairInformation.objects.get(
            id=self.minimal_pair_information2.id)
        self.minimal_pair_information1.save()
        self.minimal_pair_information3.associated_sound_id = MinimalPairInformation.objects.get(
            id=self.minimal_pair_information4.id)
        self.minimal_pair_information3.save()

    def test_quiz_display(cls):
        """

        """

        cls.selenium.get('%s%s' % (cls.live_server_url, '/quiz/1'))

        try:
            cls.selenium.find_element_by_id('first_answer').click()
        except ElementClickInterceptedException:
            play_button = cls.selenium.find_element_by_id('first_answer')
            time.sleep(1)
            ActionChains(cls.selenium).move_to_element_with_offset \
                (play_button, 0, -100).click().perform()

        try:
            cls.selenium.find_element_by_id('next').click()
            time.sleep(3)
        except ElementClickInterceptedException:
            next = cls.selenium.find_element_by_id('next')
            ActionChains(cls.selenium).move_to_element_with_offset \
                (next, 0, -100).click().perform()

        time.sleep(3)


class QuizTest(TestCase):
    """

    """

    # def setUp(self):
    #     self.user = User.objects.create_user(id=1,
    #                                          username="test",
    #                                          password="test",
    #                                          )
    #     self.phoneme_type_vowel = PhonemeType.objects.create \
    #         (id=2, type_name="Voyelles")
    #
    #     self.sub_phoneme_type_diphthong = SubPhonemeType.objects \
    #         .create(id=11
    #                 , subtype_name="Diphtongues"
    #                 , phoneme_type_id=PhonemeType.objects.get(
    #             id=self.phoneme_type_vowel.id).id)
    #
    #     self.phoneme1 = PhonemeInformation.objects.create(id=1
    #                                                       , label='eɪ'
    #                                                       , sound_file_name='eɪ.mp3'
    #                                                       , sub_phoneme_type_id=SubPhonemeType.objects.get
    #         (id=self.sub_phoneme_type_diphthong.id).id)
    #     self.phoneme2 = PhonemeInformation.objects.create(id=2
    #                                                       , label='ɛ'
    #                                                       , sound_file_name='ɛ.mp3'
    #                                                       , sub_phoneme_type_id=SubPhonemeType.objects.get
    #         (id=self.sub_phoneme_type_diphthong.id).id)
    #
    #     self.minimal_pair_category = MinimalPairCategory.objects.create(id=1
    #                                                                     , phoneme=PhonemeInformation.objects.get(
    #             id=self.phoneme1.id)
    #                                                                     ,
    #                                                                     associated_phoneme=PhonemeInformation.objects.get(
    #                                                                         id=self.phoneme2.id)
    #                                                                     ,
    #                                                                     sub_phoneme_type_id=SubPhonemeType.objects.get(
    #                                                                         id=self.sub_phoneme_type_diphthong.id)
    #                                                                     )
    #     self.minimal_pair_information1 = MinimalPairInformation.objects.create(id=1
    #                                                                            , label="taste"
    #                                                                            , ipa_label="/teɪst/"
    #                                                                            , category_id=MinimalPairCategory.objects
    #                                                                            .get(id=self.minimal_pair_category.id))
    #
    #     self.minimal_pair_information2 = MinimalPairInformation.objects.create(id=2
    #                                                                            , label="test"
    #                                                                            , ipa_label="/tɛst/"
    #                                                                            ,
    #                                                                            associated_sound_id=MinimalPairInformation.objects.get(
    #                                                                                id=self.minimal_pair_information1.id)
    #                                                                            , category_id=MinimalPairCategory.objects
    #                                                                            .get(id=self.minimal_pair_category.id))
    #     self.minimal_pair_information1.associated_sound_id = MinimalPairInformation.objects.get(
    #         id=self.minimal_pair_information2.id)
    #     self.minimal_pair_information1.save()

    def test_view_returns_last_page_if_id_page_out_of_range(self):
        """
        View return last page if page number given is out o range
        """
        session = self.client.session
        session['quiz_query'] = []
        session.save()
        response = self.client.get('/quiz/1', {'query': '', 'page': 9}
                                   )
        self.assertEquals(response.context['questions'].number, 1) # TypeError: 'NoneType' object is not subscriptable
        self.assertEqual(response.status_code, 200) # OK

    def test_save_answer(self):
        """

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
        # response = self.client.post(reverse('rolcreate'), {'name' : 'new_object'})
        response = self.client.post('/save_answer', {'answer': ['king'], 'page': ['1']})
        self.assertEqual(response.status_code, 200)

    def test_score_returns_expected_html(self):
        """
        Login page is accessible with 'login'
        """
        self.client.login(username='test', password='test')
        session = self.client.session
        session['quiz_query'] = [
            {'id': 74, 'label': 'king', 'ipa_label': '/kɪŋ/', 'associated_sound_id_id': 73, 'category_id_id': 6}
            , {'id': 75, 'label': 'thin', 'ipa_label': '/θɪn/', 'associated_sound_id_id': 76, 'category_id_id': 6}
            , {'id': 76, 'label': 'thing', 'ipa_label': '/θɪŋ/', 'associated_sound_id_id': 75, 'category_id_id': 6}
            , {'id': 77, 'label': 'ran', 'ipa_label': '/ɹæn/', 'associated_sound_id_id': 78, 'category_id_id': 6}
            , {'id': 78, 'label': 'rang', 'ipa_label': '/ɹæŋ/', 'associated_sound_id_id': 77, 'category_id_id': 6}
            , {'id': 82, 'label': 'tongue', 'ipa_label': '/tʌŋ/', 'associated_sound_id_id': 81, 'category_id_id': 6}
            , {'id': 84, 'label': 'bang', 'ipa_label': '/bæŋ/', 'associated_sound_id_id': 83, 'category_id_id': 6}
            , {'id': 86, 'label': 'hanged', 'ipa_label': '/hæŋd/', 'associated_sound_id_id': 85, 'category_id_id': 6}]
        session['score'] = None
        session['user_answers_list'] = [{'answer': 'king', 'page': '1'}
            , {'answer': 'thin', 'page': '2'}, {'answer': 'thing', 'page': '3'}
            , {'answer': 'ran', 'page': '4'}, {'answer': 'rang', 'page': '5'}
            , {'answer': 'tongue', 'page': '6'}, {'answer': 'tongue', 'page': '6'}
            , {'answer': 'bang', 'page': '7'}, {'answer': 'hand', 'page': '8'}]
        session.save()
        response = self.client.get(reverse("quiz:score", kwargs={'category_id': '1'}))
        self.assertEqual(response.status_code, 200)  # vérifier que length des deux listes est égale

    def test_save_score(self):
        """

        """
        self.client.login(username='test', password='test')
        session = self.client.session
        session['score'] = 7
        session.save()
        self.client.get(reverse('quiz:save_results', kwargs={
            'category_id': '1'}))
        # self.assertEqual(Score.objects.all().count(), 4)
        self.assertEqual(Score.objects.all().count(), 1)
