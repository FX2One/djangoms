# Generated by Django 4.0 on 2022-01-14 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicapp', '0005_available_comic_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='subscriber',
            new_name='subscribers',
        ),
    ]
