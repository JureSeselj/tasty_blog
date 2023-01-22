# Generated by Django 3.2 on 2023-01-22 18:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=20)),
                ('link', models.URLField(blank=True)),
                ('review', models.TextField(max_length=200)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
