# Generated by Django 2.0 on 2018-07-11 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180711_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='authoor',
            new_name='author',
        ),
    ]
