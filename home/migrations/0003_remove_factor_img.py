# Generated by Django 4.2 on 2023-08-02 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_factor_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factor',
            name='img',
        ),
    ]
