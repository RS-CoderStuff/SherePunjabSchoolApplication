# Generated by Django 2.0.1 on 2020-02-24 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0028_auto_20200224_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_notification_db',
            name='batch',
        ),
    ]
