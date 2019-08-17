from django.conf import settings
from django.urls import path
from .import views

app_name = 'aboutus'
urlpatterns = [
    path('', views.Aboutus_list, name='Aboutus_list'),

]
