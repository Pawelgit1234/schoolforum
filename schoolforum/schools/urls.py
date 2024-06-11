from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
    path('load_more_schools/', views.load_more_schools, name='load_more_schools'),
    path('school/<slug:slug>', views.school, name='school'),
    path('load_more_discussions/<slug:slug>', views.load_more_discussions, name='load_more_discussions'),
    path('discussion/<int:id>', views.discussion, name='discussion'),
    path('load_more_comments/<int:id>', views.load_more_comments, name='load_more_comments'),
]