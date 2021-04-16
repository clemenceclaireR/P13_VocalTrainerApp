from django.test.runner import DiscoverRunner as BaseRunner
from django.contrib.auth.models import User
from minimal_pair.models import MinimalPairCategory, MinimalPairInformation, MinimalPairWordPhonemeLetters
from ipa_board.models import SubPhonemeType, PhonemeType, PhonemeInformation, ExampleWord


class CustomTestRunner(BaseRunner):
    """
    Load the database with data to be shared between
    different TestCases classes
    """

    def setup_databases(self, *args, **kwargs):
        res = super().setup_databases(*args, **kwargs)

        self.user = (User.objects
                     .create_user
                     (id=1,
                      username="test",
                      password="test",
                      ))

        self.consonant_type = (PhonemeType.objects
                               .create(id=1,
                                       type_name="Consonnes"))

        self.vowel_type = PhonemeType.objects.create(id=2,
                                                     type_name="Voyelles")

        self.diphthong_subtype = (SubPhonemeType.objects
                                  .create(id=11
                                          , subtype_name="Diphtongues"
                                          , phoneme_type_id=PhonemeType
                                          .objects.get(id=self.vowel_type.id).id))

        self.simple_vowel_subtype = (SubPhonemeType.objects
                                     .create(id=6
                                             , subtype_name="Pré-fermées"
                                             , phoneme_type_id=PhonemeType
                                             .objects
                                             .get(id=self.vowel_type.id).id))

        self.consonants_subtype = (SubPhonemeType.objects
                                   .create(id=1
                                           , subtype_name="Occlusives"
                                           , phoneme_type_id=PhonemeType
                                           .objects.get(id=self.consonant_type.id).id))

        self.phoneme1 = (PhonemeInformation.objects
                         .create(id=1
                                 , label='eɪ'
                                 , sound_file_path='eɪ.mp3'
                                 , sub_phoneme_type_id=SubPhonemeType
                                 .objects.get(id=self.diphthong_subtype.id).id))

        self.phoneme2 = (PhonemeInformation.objects
                         .create(id=2
                                 , label='ɛ'
                                 , sound_file_path='ɛ.mp3'
                                 , sub_phoneme_type_id=SubPhonemeType
                                 .objects.get(id=self.diphthong_subtype.id).id))

        self.phoneme3 = (PhonemeInformation.objects
                         .create(id=3
                                 , label='p'
                                 , sound_file_path='p.mp3'
                                 , sub_phoneme_type_id=SubPhonemeType
                                 .objects.get(id=self.consonants_subtype.id).id))

        self.example = (ExampleWord.objects
                        .create(id=1
                                , label="Late"
                                , phoneme_id=PhonemeInformation
                                .objects.get(id=self.phoneme1.id).id))

        self.minimal_pair = (MinimalPairCategory.objects
                             .create(id=1
                                     , phoneme=PhonemeInformation
                                     .objects.get(id=self.phoneme1.id)
                                     , associated_phoneme=PhonemeInformation
                                     .objects.get(id=self.phoneme2.id)
                                     , sub_phoneme_type_id=SubPhonemeType
                                     .objects.get(id=self.diphthong_subtype.id)
                                     ))

        self.minimal_pair_information1 = (MinimalPairInformation.objects
                                          .create(id=1
                                                  , label="taste"
                                                  , ipa_label="/teɪst/"
                                                  , category_id=MinimalPairCategory
                                                  .objects
                                                  .get(id=self.minimal_pair.id)))

        self.minimal_pair_information2 = (MinimalPairInformation.objects
                                          .create(id=2
                                                  , label="test"
                                                  , ipa_label="/tɛst/"
                                                  , associated_word_id=MinimalPairInformation
                                                  .objects.get(id=self.minimal_pair_information1.id)
                                                  , category_id=MinimalPairCategory.objects
                                                  .get(id=self.minimal_pair.id)))

        self.minimal_pair_information1.associated_word_id = (MinimalPairInformation
                                                             .objects.get(id=self.minimal_pair_information2.id))
        self.minimal_pair_information1.save()

        self.phoneme_place1 = (MinimalPairWordPhonemeLetters.objects
                               .create(minimal_pair_id=MinimalPairInformation.objects
                                       .get(id=self.minimal_pair_information1.id)
                                       , letters="a"
                                       , ipa_letters="eɪ"
                                       ))

        self.phoneme_place2 = (MinimalPairWordPhonemeLetters.objects
                               .create(minimal_pair_id=MinimalPairInformation.objects
                                       .get(id=self.minimal_pair_information2.id)
                                       , letters="e"
                                       , ipa_letters="ɛ"
                                       ))

        return res

    def teardown_databases(self, *args, **kwargs):
        super().teardown_databases(*args, **kwargs)
