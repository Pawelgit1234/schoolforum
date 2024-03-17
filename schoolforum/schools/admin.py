from django.contrib import admin

from .models import School, Discussion, Comment, Image, Rating


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'city']


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'school']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'discussion', 'created_at']