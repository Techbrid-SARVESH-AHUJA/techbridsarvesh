# Generated by Django 3.1.4 on 2021-06-28 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20210628_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_project',
            name='about_1',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='basic_project',
            name='about_2',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='basic_project',
            name='about_3',
            field=models.TextField(max_length=500, null=True),
        ),
    ]