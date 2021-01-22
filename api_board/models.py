from django.db import models


class PhonemeType(models.Model):
    """
    Type of the phoneme
    """

    class Meta:
        db_table = 'phoneme_type'

    type_name = models.CharField(max_length=254
                                 , verbose_name='Type name'
                                 , help_text='Type name'
                                 , db_column='type_name'
                                 )


class SubPhonemeType(models.Model):
    """
    Sub phoneme type
    """

    class Meta:
        db_table = 'sub_phoneme_type'

    subtype_name = models.CharField(max_length=254
                                    , verbose_name='Sub Type name'
                                    , help_text='Sub Type name'
                                    , db_column='subtype_name'
                                    )
    phoneme_type = models.ForeignKey(PhonemeType
                                     , on_delete=models.CASCADE
                                     , help_text='Associated phoneme type'
                                     , db_column='phoneme_type_id'
                                     , null=True
                                     )
    order = models.IntegerField(null=True
                                , db_column='order'
                                , help_text='Order in which types are displayed in template'
                                )


class PhonemeInformation(models.Model):
    """
    Data about the different phonemes (vowels and consonants)
    """

    class Meta:
        db_table = 'phoneme_information'

    label = models.CharField(max_length=254
                             , help_text='Phoneme name'
                             , db_column='label'
                             )
    sound_file_name = models.CharField(max_length=254
                                       , help_text='Associated file name'
                                       , db_column='sound_file_name'
                                       )
    sub_phoneme_type = models.ForeignKey(SubPhonemeType
                                         , on_delete=models.CASCADE
                                         , help_text='Associated phoneme type'
                                         , db_column='sub_phoneme_type_id'
                                         , null=True
                                         )


class ExampleWord(models.Model):
    """
    Word examples linked to a phoneme
    """

    class Meta:
        db_table = 'example_word'

    phoneme = models.ForeignKey(PhonemeInformation
                                , on_delete=models.CASCADE
                                , help_text='Associated phoneme'
                                , db_column='phoneme_id'
                                )
    label = models.CharField(max_length=254
                             , help_text='Word name'
                             , db_column='label'
                             )
