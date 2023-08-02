# Generated by Django 4.2 on 2023-08-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, to='auth.permission'),
        ),
    ]