# Generated by Django 2.0.1 on 2020-02-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0023_auto_20200220_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_content_db',
            name='image',
            field=models.ImageField(upload_to='course_content'),
        ),
    ]