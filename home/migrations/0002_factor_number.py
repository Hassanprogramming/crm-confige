# Generated by Django 4.2 on 2023-08-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='number',
            field=models.FloatField(default=2, verbose_name='تعداد'),
            preserve_default=False,
        ),
    ]
