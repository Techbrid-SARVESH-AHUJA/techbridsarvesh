# Generated by Django 3.1.4 on 2021-07-01 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_auto_20210629_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arduino_project',
            name='about_3',
        ),
    ]
