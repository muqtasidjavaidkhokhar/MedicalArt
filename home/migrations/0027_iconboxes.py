# Generated by Django 2.2 on 2019-04-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_elementloader'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconBoxes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
            ],
        ),
    ]
