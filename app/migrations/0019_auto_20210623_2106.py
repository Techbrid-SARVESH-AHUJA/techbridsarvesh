# Generated by Django 3.1.4 on 2021-06-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='desc_width',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_width',
            field=models.CharField(max_length=500, null=True),
        ),
    ]