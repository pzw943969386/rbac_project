from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    jf = models.IntegerField(default=0)

class Sug(models.Model):
    fl = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    filename = models.CharField(max_length=100,default='')
    uid = models.ForeignKey('User',on_delete=models.CASCADE)
    is_sl = models.BooleanField(default=False)
    sl = models.BooleanField()
    dj = models.CharField(max_length=10)
    zxr = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)