from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=False,blank=False)
    fb_pixel = models.CharField(max_length=250,null=False,blank=False)
    url = models.CharField(max_length=25,unique=True,null=False,blank=False)
    image = models.ImageField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"