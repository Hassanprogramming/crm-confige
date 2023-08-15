from django.db import models
from django.urls import reverse

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
    dec = models.CharField(verbose_name="توضیخات", max_length=500, blank=True, null=True)
    Category = models.ForeignKey(Category, verbose_name="دسته", on_delete=models.CASCADE)
    price = models.FloatField()
    img = models.ImageField(upload_to='images/',verbose_name="تصویر محصول", blank=True, null=True)
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url
