# Generated by Django 3.2.9 on 2021-11-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('fb_pixel', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=25, unique=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
