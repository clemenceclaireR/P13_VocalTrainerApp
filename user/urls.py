from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),
    path('user_score_history', views.user_score_history, name='user_score_history'),
    path('user_score_history', views.user_score_history, name='user_score_history'),
    path('score_chart', views.score_chart, name='score_chart'),
    path('score_chart/<int:cat>', views.score_chart, name='score_chart'),
]


