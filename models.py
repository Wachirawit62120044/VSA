from django.db import models
from djongo import models
from django.contrib.auth.models import User

# Create your models here.

#class Photo(models.Model):
#    name = models.CharField(max_length=255)
#    classname = models.CharField(max_length=255)
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    Detect_pic = models.ImageField(null=True, blank = True, default='default.jpg', upload_to='pic_pics')

#    def __str__(self):
#             return f'{self.user.username} pic'

class images(models.Model): 
    name = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images/') 