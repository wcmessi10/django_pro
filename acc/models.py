from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    comment = models.TextField()
    age = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="acc/%y/%m")

    def getpic(self):#이미지 없을 경우 기본이미지
        if self.pic:
            return self.pic.url #이미지 있으면 그 이미지로(url필수)
        return "/media/noimage.png"# 없으면 정해진 사진으로