# Generated by Django 3.1.10 on 2023-06-21 05:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='exam_user',
            new_name='music_user',
        ),
    ]