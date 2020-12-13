from django.db import models
from django.contrib.auth.models import User


class MinimalPairSoundsInformation(models.Model):
    """
    Information about the sounds
    """

    class Meta:
        db_table = 'minimal_pair_sounds_information'


    sound_name = models.CharField(max_length=254
                                  , verbose_name='Sound name'
                                  , help_text='Sound name'
                                  , db_column='sound_name'
                                  )
    associated_sound_id = models.ForeignKey('self'
                                            , on_delete=models.CASCADE
                                            , help_text='Associated sound'
                                            , db_column='associated_sound_id'
                                            )
