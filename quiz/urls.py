from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('quiz/<int:category_id>', views.quiz, name='quiz'),
    path('score/<int:category_id>', views.score, name='score'),
    path('save_answer', views.save_answer, name='save_answer'),
    # path('save_results/<int:category_id>', views.save_results, name='save_results'),
]
