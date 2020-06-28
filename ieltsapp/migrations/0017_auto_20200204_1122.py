# Generated by Django 2.0.1 on 2020-02-04 05:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0016_auto_20200127_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_db',
            old_name='description',
            new_name='meta_description',
        ),
        migrations.RenameField(
            model_name='blog_db',
            old_name='keywords',
            new_name='meta_keywords',
        ),
        migrations.AddField(
            model_name='blog_db',
            name='meta_title',
            field=models.CharField(default=datetime.datetime(2020, 2, 4, 5, 52, 18, 946333, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]