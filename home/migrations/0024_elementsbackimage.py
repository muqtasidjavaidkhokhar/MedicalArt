# Generated by Django 2.2 on 2019-04-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20190418_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementsBackImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
