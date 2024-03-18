from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('school/<slug:slug>', views.school, name='school'),
]