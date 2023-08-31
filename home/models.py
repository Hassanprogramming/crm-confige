from django.db import models
from account.models import *
from product.models import *
from account.models import *
from tinymce import models as tinymce_models
from extensions.utils import jalali_converter


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
    dec = tinymce_models.HTMLField(verbose_name="توضیحات", max_length=1000)
    dec_2 = tinymce_models.HTMLField("توضیحات بیشتر", max_length=1000)
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
    
    def jtime(self):
        return jalali_converter(self.date)


class service(models.Model):
    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = "خدمات"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , verbose_name="مشتری", on_delete=models.CASCADE)
    name_service = models.CharField(verbose_name="نام خدمات", max_length=100)
    date = models.DateTimeField(verbose_name="تاریخ ثبت", auto_now_add=True)
    dec = tinymce_models.HTMLField(verbose_name="توضیحات", max_length=1000)
    dec_2 = tinymce_models.HTMLField("توضیحات بیشتر", max_length=1000)
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
    
    def jtime(self):
        return jalali_converter(self.date)
    
