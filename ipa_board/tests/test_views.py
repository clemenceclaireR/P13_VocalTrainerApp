import time
from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from ipa_board.models import SubPhonemeType, PhonemeType, \
    PhonemeInformation, ExampleWord


class IPABoardTest(TestCase):
    """

    """

    def test_index_is_accessible(self):
        """
        Index page returns success http request
        """
        response = self.client.post(reverse("ipa_board:index"))
        self.assertTrue(response.status_code, 200)

    def test_consonant_table_is_accessible(self):
        """

        """
        response = self.client.post(reverse("ipa_board:consonant_table"))
        self.assertTrue(response.status_code, 200)

    def test_simple_vowels_table_is_accessible(self):
        """

        """
        response = self.client.post(reverse("ipa_board:simple_vowel_table"))
        self.assertTrue(response.status_code, 200)

    def test_vowels_type_menu_expected_html(self):
        """

        """
        response = self.client.get(reverse("ipa_board:vowel_menu"))
        self.assertTemplateUsed(response, 'ipa_board/vowel_menu.html')

    def test_ipa_board_menu_expected_html(self):
        """

        """
        response = self.client.get(reverse("ipa_board:ipa_board_menu"))
        self.assertTemplateUsed(response, 'ipa_board/menu_selection.html')


class IPABoardSeleniumTest(StaticLiveServerTestCase):
    """
    Simulates user behavior on IPA diagram
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

    def setUp(cls):
        cls.vowel_type = PhonemeType.objects.create(id=1, type_name="Voyelles")
        cls.diphthong_type = SubPhonemeType.objects.create(id=11,
                                                           subtype_name="Diphtongues",
                                                           phoneme_type_id=PhonemeType.objects.get(
                                                               id=cls.vowel_type.id).id)
        cls.phoneme = PhonemeInformation.objects.create(id=1
                                                        , label='eɪ'
                                                        , sound_file_name='eɪ.mp3'
                                                        , sub_phoneme_type_id=SubPhonemeType.objects.get
            (id=cls.diphthong_type.id).id)

        cls.example = ExampleWord.objects.create(id=1
                                                 , label="Late"
                                                 , phoneme_id=PhonemeInformation.objects.get
            (id=cls.phoneme.id).id)

    def test_diphthong_diagram_display(cls):
        """

        """
        cls.selenium.get('%s%s' % (cls.live_server_url, '/diphthong_table'))

        cls.selenium.find_element_by_id('collapse_eɪ').click()

        try:
            time.sleep(1)
            cls.selenium.find_element_by_id('play_Late').click()
        except ElementClickInterceptedException:
            play_button = cls.selenium.find_element_by_id('play_Late')
            time.sleep(1)
            ActionChains(cls.selenium).move_to_element_with_offset\
                (play_button, 0, -100).click().perform()

        time.sleep(1)
