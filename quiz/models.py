from django.db import models
from django.contrib.auth.models import User
from minimal_pair.models import MinimalPairCategory


class Score(models.Model):
    """
    Keep tracks on the user scores on quiz
    """

    class Meta:
        db_table = 'score'

    user_id = models.ForeignKey(User
                                , on_delete=models.CASCADE
                                , db_index=True
                                , verbose_name='User'
                                , help_text='User'
                                , db_column='user_id'
                                )
    score = models.IntegerField(null=True
                                , blank=True
                                , db_column='score'
                                )
    date = models.DateTimeField(null=True
                                , blank=True
                                , db_column='date'
                                , auto_now_add = True
                                )

    minimal_pair_category_id = models.ForeignKey(MinimalPairCategory
                                                 , on_delete=models.CASCADE
                                                 , verbose_name='Score associated category'
                                                 , help_text='Score associated category'
                                                 , db_column='minimal_pair_category_id'
                                                 )
