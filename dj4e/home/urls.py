from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
#    path('', views.index, name='home'),
    path('', TemplateView.as_view(template_name='main.html'), name='main'),

]
