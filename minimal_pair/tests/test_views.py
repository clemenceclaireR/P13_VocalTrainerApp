from django.test import TestCase
from django.urls import reverse
from minimal_pair.models import MinimalPairCategory, MinimalPairInformation, MinimalPairWordPhonemePlace
from ipa_board.models import SubPhonemeType, PhonemeType, PhonemeInformation


class MinimalPairTest(TestCase):
    """

    """

    # def setUp(self):
        # self.phoneme_type_vowel = PhonemeType.objects.create \
        #     (id=2, type_name="Voyelles")
        #
        # self.sub_phoneme_type_diphthong = SubPhonemeType.objects \
        #     .create(id=11
        #             , subtype_name="Diphtongues"
        #             , phoneme_type_id=PhonemeType.objects.get(
        #         id=self.phoneme_type_vowel.id).id)

        # self.phoneme1 = PhonemeInformation.objects.create(id=1
        #                                                   , label='eɪ'
        #                                                   , sound_file_name='eɪ.mp3'
        #                                                   , sub_phoneme_type_id=SubPhonemeType.objects.get
        #     (id=self.sub_phoneme_type_diphthong.id).id)
        # self.phoneme2 = PhonemeInformation.objects.create(id=2
        #                                                   , label='ɛ'
        #                                                   , sound_file_name='ɛ.mp3'
        #                                                   , sub_phoneme_type_id=SubPhonemeType.objects.get
        #     (id=self.sub_phoneme_type_diphthong.id).id)

        # self.minimal_pair_category = MinimalPairCategory.objects.create(id=1
        #                                                                 , phoneme=PhonemeInformation.objects.get(
        #         id=self.phoneme1.id)
        #                                                                 ,
        #                                                                 associated_phoneme=PhonemeInformation.objects.get(
        #                                                                     id=self.phoneme2.id)
        #                                                                 ,
        #                                                                 sub_phoneme_type_id=SubPhonemeType.objects.get(
        #                                                                     id=self.sub_phoneme_type_diphthong.id)
        #                                                                 )
        #
        # self.minimal_pair_information1 = MinimalPairInformation.objects.create(id=1
        #                                                                        , label="taste"
        #                                                                        , ipa_label="/teɪst/"
        #                                                                        , category_id=MinimalPairCategory.objects
        #                                                                        .get(id=self.minimal_pair_category.id))
        #
        # self.minimal_pair_information2 = MinimalPairInformation.objects.create(id=2
        #                                                                        , label="test"
        #                                                                        , ipa_label="/tɛst/"
        #                                                                        ,
        #                                                                        associated_sound_id=MinimalPairInformation.objects.get(
        #                                                                            id=self.minimal_pair_information1.id)
        #                                                                        , category_id=MinimalPairCategory.objects
        #                                                                        .get(id=self.minimal_pair_category.id))

        # self.minimal_pair_information1.associated_sound_id = MinimalPairInformation.objects.get(
        #     id=self.minimal_pair_information2.id)
        # self.minimal_pair_information1.save()

        # self.phoneme_place1 = MinimalPairWordPhonemePlace.objects.create(minimal_pair_id=MinimalPairInformation.objects
        #                                                                  .get(id=self.minimal_pair_information1.id)
        #                                                                  , letters="a"
        #                                                                  , ipa_letters="eɪ"
        #                                                                  )
        #
        # self.phoneme_place2 = MinimalPairWordPhonemePlace.objects.create(minimal_pair_id=MinimalPairInformation.objects
        #                                                                  .get(id=self.minimal_pair_information2.id)
        #                                                                  , letters="e"
        #                                                                  , ipa_letters="ɛ"
        #                                                                  )

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
        response = self.client.get(reverse('minimal_pair:minimal_pair_table', kwargs={'phoneme': '1'}))
        self.assertTemplateUsed(response, 'minimal_pair/minimal_pair_table.html')
