# Generated by Django 4.2.1 on 2023-07-15 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialbook', '0008_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 20, 32, 38, 234993)),
        ),
    ]
