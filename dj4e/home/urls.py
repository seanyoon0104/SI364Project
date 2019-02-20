from django.urls import path
from . import views

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.index, name='home'),
]
