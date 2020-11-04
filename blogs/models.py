from django.db import models
from django.utils import timezone
from django.contrib.auth.models	import User
from django.utils.timezone import now


class BlogsModel(models.Model):
    STATUS_CHOICES = (
        ('Air Force', 'Air Force'),
        ('Army', 'Army'),
        ('Navy', 'Navy'),
        ('Afcat', 'Afcat'),
        ('CDS', 'CDS'),
        ('NDA', 'NDA'),
        ('NCC', 'NCC'),
    )
    blog_title = models.CharField(max_length=500)
    type = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Defence')
    intro = models.CharField(max_length=500)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, default=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.blog_title


class Customers(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    querry = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name