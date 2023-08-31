from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from extensions.utils import jalali_converter


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "بالا دسته"
        verbose_name_plural = "بالا دسته"
        
    name = models.CharField(verbose_name="نام دسته", max_length=100)
    display = models.BooleanField(verbose_name="نمایش داده شود؟")

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"
        
    name = models.CharField(verbose_name="نام محصول", max_length=100)
    dec = tinymce_models.HTMLField(verbose_name="توضیخات", max_length=500, blank=True, null=True)
    Category = models.ForeignKey(Category, verbose_name="دسته", on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="قیمت")
    number = models.IntegerField(verbose_name="تعداد محصول در انبار")
    date_created = models.DateTimeField(verbose_name="تاریخ ثبت محصول", auto_now_add=True)
    img = models.ImageField(upload_to='images/',verbose_name="تصویر محصول", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def jtime(self):
        return jalali_converter(self.date_created)
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url
