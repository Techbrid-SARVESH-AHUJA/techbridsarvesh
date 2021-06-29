# Generated by Django 3.1.4 on 2021-06-23 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_blog_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200, null=True)),
                ('site_short_name', models.CharField(max_length=200, null=True)),
                ('site_logo', models.ImageField(upload_to='static')),
                ('site_description', models.CharField(max_length=200, null=True)),
                ('site_mail', models.CharField(max_length=200, null=True)),
                ('site_phone', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='company',
        ),
    ]