# Generated by Django 2.2.10 on 2021-06-12 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210612_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='time',
        ),
    ]