# Generated by Django 3.1.4 on 2021-06-22 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210622_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='image',
            new_name='company_logo',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
    ]
