# Generated by Django 2.2.2 on 2019-06-23 12:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190623_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 23, 12, 7, 10, 932729, tzinfo=utc), verbose_name=datetime.datetime(2019, 6, 23, 12, 7, 10, 932729, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 23, 12, 7, 10, 932729, tzinfo=utc)),
        ),
    ]
