from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.home_view, name='home'),
    path('load_more_schools/', views.load_more_schools, name='load_more_schools'),
    path('school/<slug:slug>', views.school_view, name='school'),
    path('load_more_discussions/<slug:slug>', views.load_more_discussions, name='load_more_discussions'),
    path('discussion/<int:id>', views.discussion_view, name='discussion'),
    path('discussion_rating/', views.change_discussion_rating, name="discussion_rating"),
    path('comment_rating/', views.change_comment_rating, name="comment_rating"),
    path('load_more_comments/<int:id>', views.load_more_comments, name='load_more_comments'),
]