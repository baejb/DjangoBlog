import os.path

from django.contrib.auth.models import User
from django.db import models
from turtle import mode

# Create your models here.
class Category(models.Model):
    

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    hook_msg = models.TextField(blank=True)

    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    attached_file = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.attached_file.name)