from random import randint
from django.contrib import admin, messages
from django.core.mail import send_mail,EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from Defence_Blogs import settings
from blogs.models import BlogsModel,Customers

# Create your views here.
def home(request):
    post_id = randint(1,len(BlogsModel.objects.all()))
    sample_post = BlogsModel.objects.get(id=post_id)

    data = BlogsModel.objects.all()
    p = Paginator(data, 6)
    page_no = request.GET.get('pno')
    if page_no == "view_all":
        return redirect('all_blogs')
    else:
        page = p.page(1)
    return render(request, 'index.html', {'data': page,"footer":data, 'sample_post': sample_post})


def allBlogs(request):
    return render(request, 'all_blogs.html',{"data": BlogsModel.objects.all()})


def blogs(request):
    blog_type = request.GET.get('type')
    data = BlogsModel.objects.filter(type=blog_type)
    footer_page = BlogsModel.objects.all()
    p = Paginator(data, 4)

    page_no = request.GET.get('pno')
    if page_no:
        page = p.page(page_no)
    else:
        page = p.page(1)
    return render(request, 'blogs.html', {'footer': footer_page,'data': page,"type": blog_type})


def post(request):
    post_id = request.GET.get('post')
    post = BlogsModel.objects.get(id=post_id)
    return render(request,'post.html', {'data': post})


def get_feedback(request):
    user = request.POST.get('name')
    message = request.POST.get('message')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    try:
        send_mail("reply to the subject :"+subject, "Your message is : "+message, settings.EMAIL_HOST_USER,[email,], fail_silently=False)
        Customers(name=user, email=email, querry=subject, message=message).save()
        messages.success(request, 'Thanks for reaching us.')
    except:
        messages.error(request, 'Please enter a valid mail id.')
    return redirect('contact')
