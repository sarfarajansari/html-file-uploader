# Generated by Django 3.1.4 on 2021-04-16 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlmanager', '0004_project_projectfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]
