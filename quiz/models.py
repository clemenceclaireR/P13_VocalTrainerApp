from django.db import models
from django.contrib.auth.models import User


class Score(models.Model):
    """
    Keep tracks on the user scores on quiz
    """

    class Meta:
        db_table = 'score'

    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                db_index=True,
                                verbose_name='User',
                                help_text='User'
                                , db_column='user_id'
                                )
    score = models.IntegerField(null=True
                              , blank=True
                              , db_column='score'
                              )
    date = models.DateTimeField(null=True
                                , blank=True
                                , db_column='date'
                                )
