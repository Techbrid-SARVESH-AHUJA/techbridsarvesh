# Generated by Django 3.1.4 on 2021-06-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_company_company_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]