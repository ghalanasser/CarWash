from django.urls import path
from . import views

app_name = 'Client_Pages'
urlpatterns = [
    path('', views.home, name='home'),
]