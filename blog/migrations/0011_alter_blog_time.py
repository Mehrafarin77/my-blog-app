# Generated by Django 5.0.7 on 2024-08-17 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blog_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 17, 13, 50, 52, 743151)),
        ),
    ]