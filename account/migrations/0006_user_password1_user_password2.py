# Generated by Django 4.2 on 2023-08-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]
