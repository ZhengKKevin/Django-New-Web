# Generated by Django 2.0 on 2018-08-02 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payinfo', '0002_payinfoorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='payinfoorder',
            name='status',
            field=models.SmallIntegerField(null=True),
        ),
    ]
