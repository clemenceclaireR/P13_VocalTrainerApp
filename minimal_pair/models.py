from django.db import models
from django.contrib.auth.models import User
from ipa_board.models import PhonemeInformation, SubPhonemeType


class MinimalPairCategory(models.Model):
    """
    Minimal pairs categories
    """

    class Meta:
        db_table = "minimal_pair_category"

    phoneme = models.ForeignKey(PhonemeInformation
                                , on_delete=models.CASCADE
                                , verbose_name='First phoneme'
                                , help_text='Phoneme'
                                , db_column='phoneme'
                                , related_name="first_phoneme_id"
                                )
    associated_phoneme = models.ForeignKey(PhonemeInformation
                                           , on_delete=models.CASCADE
                                           , verbose_name='Associated phoneme'
                                           , help_text='Associated phoneme'
                                           , db_column='associated_phoneme'
                                           , null=True
                                           , related_name="second_phoneme_id"
                                           )
    sub_phoneme_type_id = models.ForeignKey(SubPhonemeType
                                            , on_delete=models.CASCADE
                                            , help_text='Associated phoneme type'
                                            , db_column='sub_phoneme_type_id'
                                            )


class MinimalPairInformation(models.Model):
    """
    Information about the minimal pair sounds
    """

    class Meta:
        db_table = 'minimal_pair_information'

    label = models.CharField(max_length=254
                             , verbose_name='Sound name'
                             , help_text='Sound name'
                             , db_column='label'
                             )
    ipa_label = models.CharField(max_length=254
                                 , verbose_name='IPA sound name'
                                 , help_text='IPA sound name'
                                 , db_column='ipa_label'
                                 )
    associated_sound_id = models.ForeignKey('self'
                                            , on_delete=models.CASCADE
                                            , help_text='Associated sound'
                                            , db_column='associated_sound_id'
                                            )
    category_id = models.ForeignKey(MinimalPairCategory
                                    , on_delete=models.CASCADE
                                    , help_text='Category of the minimal pair sound'
                                    , db_column='category_id'
                                    )


class MinimalPairWordPhonemePlace(models.Model):
    """
    Show the phoneme place in word entry in MinimalPairInformation
    """

    class Meta:
        db_table = 'minimal_pair_word_phoneme_place'

    minimal_pair_id = models.OneToOneField(
        MinimalPairInformation
        , primary_key=True
        , on_delete=models.CASCADE
        , db_column='minimal_pair_id'
        , help_text='Associated minimal pair'
    )
    letters = models.CharField(max_length=254
                               , verbose_name='Phoneme letters'
                               , help_text='Phoneme letters'
                               , db_column='letters'
                               , null=True
                               )

    ipa_letters = models.CharField(max_length=254
                                   , verbose_name='IPA phoneme letters'
                                   , help_text='IPA phoneme letters'
                                   , db_column='ipa_letters'
                                   , null=True
                                   )
