# Generated by Django 2.2 on 2019-04-18 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_servicestabs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicestabs',
            name='main_title',
        ),
    ]
