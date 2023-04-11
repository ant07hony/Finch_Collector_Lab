# setup home path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('all_finches/', views.finches_index, name='index')
]
