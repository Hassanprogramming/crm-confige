from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="نام دسته", max_length=100)
    display = models.BooleanField(verbose_name="نمایش داده شود؟")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="نام محصول", max_length=100)
    dec = models.CharField(verbose_name="توضیخات", max_length=500, blank=True, null=True)
    Category = models.ForeignKey(Category, verbose_name="دسته", on_delete=models.CASCADE)
    img = models.ImageField(verbose_name="تصویر محصول")
    
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url