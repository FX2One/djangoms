# Generated by Django 4.0 on 2022-01-11 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comics',
            new_name='Comic',
        ),
    ]
