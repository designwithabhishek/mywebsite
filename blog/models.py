from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    created=models.DateTimeField(timezone.now())
    content=models.TextField()
    image=models.ImageField(upload_to='post')

    def __str__(self):
        return self.title

class Comments(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    content=models.TextField()
    created=models.DateTimeField(timezone.now(),default=timezone.now())
    images=models.ImageField(upload_to='user')