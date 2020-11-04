from django.contrib import admin
from blogs.models import BlogsModel


# Register your models here.

@admin.register(BlogsModel)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','blog_title','type','intro','author','published_time')


