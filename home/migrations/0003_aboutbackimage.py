# Generated by Django 2.2 on 2019-04-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_appointments'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBackImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
