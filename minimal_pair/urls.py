from django.urls import path
from .views import *

app_name = 'minimal_pair'

urlpatterns = [
    path('minimal_pair_consonant_menu', minimal_pair_consonant_menu, name='minimal_pair_consonant_menu'),
    path('minimal_pair_vowel_menu', minimal_pair_vowels_type_menu, name='minimal_pair_vowels_type_menu'),
    path('minimal_pair_diphthong_menu', minimal_pair_diphthong_menu, name='minimal_pair_diphthong_menu'),
    path('minimal_pair_menu', minimal_pair_menu, name='minimal_pair_menu'),
    path('minimal_pair_table/<int:phoneme>', minimal_pair_table, name='minimal_pair_table'),
]


