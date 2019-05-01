# Generated by Django 2.2 on 2019-04-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delete_servicestabs'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesTabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tab_title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
            ],
        ),
    ]
