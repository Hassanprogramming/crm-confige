# Generated by Django 4.1.4 on 2023-07-26 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('Category', models.CharField(max_length=100, verbose_name='دسته')),
                ('date', models.DateTimeField(verbose_name='تاریخ ثبت')),
                ('dec', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('checks', models.BooleanField(verbose_name='پرداخت شده؟')),
                ('price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('img', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]