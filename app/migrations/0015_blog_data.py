# Generated by Django 3.1.4 on 2021-06-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210622_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]