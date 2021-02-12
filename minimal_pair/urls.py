from django.urls import path
from . import views

app_name = 'minimal_pair'

urlpatterns = [
    path('minimal_pair_consonant_menu', views.minimal_pair_consonant_menu
         , name='minimal_pair_consonant_menu'),
    path('minimal_pair_vowel_menu', views.minimal_pair_vowels_type_menu
         , name='minimal_pair_vowels_type_menu'),
    path('minimal_pair_diphthong_menu', views.minimal_pair_diphthong_menu
         , name='minimal_pair_diphthong_menu'),
    path('minimal_pair_menu', views.minimal_pair_menu
         , name='minimal_pair_menu'),
    path('minimal_pair_table/<int:phoneme>', views.minimal_pair_table
         , name='minimal_pair_table'),
]
