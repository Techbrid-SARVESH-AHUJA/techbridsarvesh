# Generated by Django 3.1.4 on 2021-08-18 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_auto_20210702_1937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='code',
            new_name='python_code',
        ),
    ]
