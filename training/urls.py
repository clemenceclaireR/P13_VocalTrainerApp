from django.urls import path
from . import views

app_name = 'training'

urlpatterns = [
    path('minimal_pair', views.minimal_pair, name='minimal_pair'),
]


