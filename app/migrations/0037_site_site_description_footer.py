# Generated by Django 3.1.4 on 2021-06-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20210625_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='site_description_footer',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]