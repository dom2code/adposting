# Generated by Django 2.1.15 on 2022-04-18 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_auto_20220418_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
