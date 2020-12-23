from django.urls import path
from . import views

app_name = 'api_board'

urlpatterns = [
    path('', views.index, name='index'),
    path('api_board_menu', views.api_board_menu, name='api_board_menu'),
    path('consonant_table', views.consonant_table, name='consonant_table'),
    path('diphthong_table', views.diphthong_table, name='diphthong_table'),
    path('vowel_menu', views.vowels_type_menu, name='vowel_menu'),
    path('simple_vowel_table', views.simple_vowel_table, name='simple_vowel_table'),
]


