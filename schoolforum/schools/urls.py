from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('load_more_schools/', views.load_more_schools, name='load_more_schools'),
    path('school/<slug:slug>', views.school, name='school'),
]