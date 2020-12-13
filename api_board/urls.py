from django.urls import path
from . import views

app_name = 'api_board'

urlpatterns = [
    path('', views.index, name='index'),
    path('api_board_menu', views.api_board_menu, name='api_board_menu'),
    path('consonant_table', views.consonant_table, name='consonant_table'),
]


