# Generated by Django 3.2 on 2023-01-21 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='user',
        ),
    ]
