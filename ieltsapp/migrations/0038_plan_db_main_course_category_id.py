# Generated by Django 2.0.1 on 2020-03-19 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ieltsapp', '0037_auto_20200316_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan_db',
            name='main_course_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Main_Course_Category_Db'),
        ),
    ]
