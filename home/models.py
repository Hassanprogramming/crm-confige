from django.db import models
from account.models import *
from product.models import *
from account.models import *

# Create your models here.

class Factor(models.Model):
    class Meta:
        verbose_name = "فاکتور ها "
        verbose_name_plural = "فاکتور ها "
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , verbose_name="مشتری", on_delete=models.CASCADE)
    name = models.ForeignKey(Product, verbose_name="نام محصول", max_length=100, on_delete=models.CASCADE, blank=True, null=True)
    Category = models.ForeignKey(Category, verbose_name="دسته", max_length=100, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="تاریخ ثبت", auto_now_add=True)
    dec = models.TextField(verbose_name="توضیحات", max_length=500)
    checks = models.BooleanField(verbose_name="پرداخت شده؟")
    number = models.FloatField(verbose_name="تعداد")
    price = models.FloatField(verbose_name="قیمت", blank=True, null=True)
    total_price = models.FloatField(verbose_name="مبلغ کل")
    img = models.ImageField(upload_to="images/", blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class service(models.Model):
    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = "خدمات"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , verbose_name="مشتری", on_delete=models.CASCADE)
    name_service = models.CharField(verbose_name="نام خدمات", max_length=100)
    date = models.DateTimeField(verbose_name="تاریخ ثبت", auto_now_add=True)
    dec = models.TextField(verbose_name="توضیحات", max_length=500)
    checks = models.BooleanField(verbose_name="پرداخت شده؟")
    number = models.FloatField(verbose_name="تعداد", blank=True, null=True)
    price = models.FloatField(verbose_name="قیمت", blank=True, null=True)
    total_price = models.FloatField(verbose_name="مبلغ کل")
    img = models.ImageField(upload_to="images/", blank=True, null=True)
    
    def __str__(self):
        return self.name_service
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url
    
