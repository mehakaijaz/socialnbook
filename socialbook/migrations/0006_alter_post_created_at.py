# Generated by Django 4.2.1 on 2023-06-20 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialbook', '0005_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 20, 20, 13, 52, 264860)),
        ),
    ]
