from django.contrib import admin
from blogs.models import BlogsModel,Customers


# Register your models here.

@admin.register(BlogsModel)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','blog_title','type','intro','author','published_time')


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'querry','message')


