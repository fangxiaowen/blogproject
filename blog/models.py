# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """
    Django ???????? models.Model ??
    Category ??????????? name ?????
    CharField ?????? name ?????,CharField ????,
    CharField ? max_length ?????????,????????????????????
    ?? Django ????????????????,??????? DateTimeField????? IntegerField ???
    Django ????????????:
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Tag(models.Model):
    """
    ?? Tag ?????,? Category ???
    ????????? models.Model ?!
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    ?????????????,???????????
    """

    # ????
    title = models.CharField(max_length=70)

    # ????,????? TextField?
    # ????????????? CharField,???????????????????,???? TextField ????????
    body = models.TextField()

    # ????????????????????????,???????? DateTimeField ???
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # ????,????????,?????? CharField ??????????,???????
    # ?? CharField ? blank=True ?????????????
    excerpt = models.CharField(max_length=200, blank=True)

    # ???????,??????????????????
    # ?????????????????????????????????,?????????????
    # ????????????????,??????????????,???????? ForeignKey,??????????
    # ???????,???????????,??????????????,?????? ManyToManyField,?????????????
    # ??????????????,????? tags ??? blank=True?
    # ???? ForeignKey?ManyToManyField ???,????????,????????:
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # ????,?? User ?? django.contrib.auth.models ????
    # django.contrib.auth ? Django ?????,???????????????????,User ? Django ?????????????
    # ?????? ForeignKey ???? User ??????
    # ?????????????????,?????????????,????????????,? Category ???
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        #print('fuuuuu!!!')
        return reverse('blog:detail', kwargs={'pk': self.pk})