# Generated by Django 3.1.4 on 2021-06-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_certification'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='certification',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]
