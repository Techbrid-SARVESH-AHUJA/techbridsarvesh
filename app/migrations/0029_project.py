# Generated by Django 3.1.4 on 2021-06-24 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='static')),
                ('video_link', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
