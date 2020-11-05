from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from Defence_Blogs import settings
from blogs import views


admin.site.site_header = 'Defence Blogs'
admin.site.site_title= 'Defence Blogs Admin'
admin.site.index_title = 'Welcome to Defence Blogs | Admin'

urlpatterns = [
    path('', views.home, name='home'),
    path('Blogs/', views.blogs, name='blogs'),
    path('All_Blogs/', views.allBlogs, name='all_blogs'),
    path('Post/', views.post, name='post'),
    path('Contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('Feedback/', views.get_feedback, name='get_feedback')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
