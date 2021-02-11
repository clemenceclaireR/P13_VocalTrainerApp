from django.test import TestCase
from django.urls import reverse
from minimal_pair.models import MinimalPairCategory
from ipa_board.models import SubPhonemeType, PhonemeType, PhonemeInformation


class MinimalPairTest(TestCase):
    """

    """

    def setUp(self):
        self.phoneme_type_vowel = PhonemeType.objects.create\
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
                                                          , label='aɪ'
                                                          , sound_file_name='aɪ.mp3'
                                                          , sub_phoneme_type_id=SubPhonemeType.objects.get
            (id=self.sub_phoneme_type_diphthong.id).id)

        self.minimal_pair = MinimalPairCategory.objects.create(id=1
                                                               , phoneme=PhonemeInformation.objects.get(
                id=self.phoneme1.id)
                                                               , associated_phoneme=PhonemeInformation.objects.get(
                id=self.phoneme2.id)
                                                               , sub_phoneme_type_id=SubPhonemeType.objects.get(
                id=self.sub_phoneme_type_diphthong.id)
                                                               )

    def test_minimal_pair_menu_return_expected_html(self):
        """
        Minimal pair menu is accessible with reverse path
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_menu.html')

    def test_minimal_pair_consonant_menu_return_expected_html(self):
        """
        Minimal pair menu is accessible with reverse path
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_consonant_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_consonant_menu.html')

    def test_minimal_pair_vowels_type_menu_return_expected_html(self):
        """
        Minimal pair menu is accessible with reverse path
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_vowels_type_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_vowel_menu.html')

    def test_minimal_pair_diphthong_menu_return_expected_html(self):
        """
        Minimal pair menu is accessible with reverse path
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_diphthong_menu'))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_diphthong_menu.html')

    def test_minimal_pair_table_return_expected_html(self):
        """
        Minimal pair menu is accessible with reverse path
        """
        response = self.client.get(reverse('minimal_pair:minimal_pair_table', args=(1,)))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_table.html')


