# Generated by Django 3.1.4 on 2021-04-16 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlmanager', '0006_auto_20210416_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectfile',
            name='filename',
        ),
    ]
