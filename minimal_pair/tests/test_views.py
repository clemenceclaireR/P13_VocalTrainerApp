from django.test import TestCase
from django.urls import reverse
from minimal_pair.models import MinimalPairCategory, MinimalPairInformation, MinimalPairWordPhonemePlace
from ipa_board.models import SubPhonemeType, PhonemeType, PhonemeInformation


class MinimalPairTest(TestCase):
    """
    Unit tests for Minimal pair app
    """

    def test_minimal_pair_menu_return_expected_html(self):
        """
        Minimal pair menu is returned successfully
        with its associated template
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_menu.html')
        self.assertTrue(response.status_code, 200)

    def test_minimal_pair_consonant_menu_return_expected_html(self):
        """
        Minimal pair consonant menu is returned successfully
        with its associated template
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_consonant_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_consonant_menu.html')
        self.assertTrue(response.status_code, 200)

    def test_minimal_pair_vowels_type_menu_return_expected_html(self):
        """
        Minimal pair vowel type menu is returned successfully
        with its associated template
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_vowels_type_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_vowel_menu.html')
        self.assertTrue(response.status_code, 200)

    def test_minimal_pair_diphthong_menu_return_expected_html(self):
        """
        Minimal pair diphthong menu is returned successfully
        with its associated template
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_diphthong_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_diphthong_menu.html')
        self.assertTrue(response.status_code, 200)

    def test_minimal_pair_simple_simple_vowel_menu_return_expected_html(self):
        """
        Minimal pair simple vowels menu is returned
        successfully with its associated template
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_simple_vowel_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_simple_vowel_menu.html')
        self.assertTrue(response.status_code, 200)


    def test_minimal_pair_table_return_expected_html(self):
        """
        Phoneme associated minimal pair menu table
        is returned successfully with its associated template
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_table'
                                           , kwargs={'phoneme': '1'}))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_table.html')
        self.assertTrue(response.status_code, 200)
