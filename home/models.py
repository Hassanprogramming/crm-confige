from django.db import models
from account.models import *
# Create your models here.

class Factor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="نام محصول", max_length=100)
    Category = models.CharField(verbose_name="دسته", max_length=100)
    date = models.DateTimeField(verbose_name="تاریخ ثبت")
    dec = models.CharField(verbose_name="توضیحات", max_length=500)
    checks = models.BooleanField(verbose_name="پرداخت شده؟")
    number = models.FloatField(verbose_name="تعداد")
    price = models.FloatField()
    total_price = models.FloatField()
    # img = models.ImageField()
    
    def __str__(self):
        return self.name,(str.user)
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.img.url
    #     except:
    #         url = ''
    #     return url
