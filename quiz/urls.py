from django.urls import path
from .views import *

app_name = 'quiz'

urlpatterns = [
    path('quiz/<int:category_id>', quiz, name='quiz'),
    path('score/<int:category_id>', score, name='score'),
    path('save_answer', save_answer, name='save_answer'),
]


