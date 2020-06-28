# Generated by Django 2.0.1 on 2019-12-24 07:15

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(0, 'guest'), (1, 'teacher or admin'), (2, 'student'), (3, 'paid')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Batch_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('start_time', models.CharField(max_length=1000)),
                ('end_time', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('students', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Batch_Db',
            },
        ),
        migrations.CreateModel(
            name='Blog_Category_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Blog_Category_Db',
            },
        ),
        migrations.CreateModel(
            name='Blog_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='blog_photo')),
                ('slug', models.SlugField(unique=True)),
                ('trash', models.BooleanField(default=1)),
                ('description', models.CharField(max_length=1000)),
                ('keywords', models.CharField(max_length=500)),
                ('details', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Blog_Category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Blog_Category_Db')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Blog_Db',
            },
        ),
        migrations.CreateModel(
            name='Course_Content_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('keywords', models.CharField(max_length=1000)),
                ('details', models.CharField(blank=True, max_length=3000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Course_Content_Db',
            },
        ),
        migrations.CreateModel(
            name='Course_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='course_photo')),
                ('meta_title', models.CharField(max_length=100)),
                ('meta_description', models.CharField(max_length=1000)),
                ('meta_keywords', models.CharField(max_length=1000)),
                ('details', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Course_Db',
            },
        ),
        migrations.CreateModel(
            name='Faq_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('keywords', models.CharField(max_length=1000)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Faq_Db',
            },
        ),
        migrations.CreateModel(
            name='Gallery_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_photo', models.FileField(upload_to='gallery_photo')),
                ('alternate_text', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Gallery_Db',
            },
        ),
        migrations.CreateModel(
            name='Main_Course_Category_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Main_Course_Category_Db',
            },
        ),
        migrations.CreateModel(
            name='Notification_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Notification_Db',
            },
        ),
        migrations.CreateModel(
            name='Sub_Course_Category_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('main_course_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Main_Course_Category_Db')),
            ],
            options={
                'db_table': 'Sub_Course_Category_Db',
            },
        ),
        migrations.CreateModel(
            name='Super_Course_Category_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('main_course_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Main_Course_Category_Db')),
            ],
            options={
                'db_table': 'Super_Course_Category_Db',
            },
        ),
        migrations.CreateModel(
            name='Testimonial_Db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_photo', models.FileField(upload_to='client_photo')),
                ('review', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Testimonial_Db',
            },
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10)),
                ('exp_date', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_Profile',
            },
        ),
        migrations.AddField(
            model_name='sub_course_category_db',
            name='super_course_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Super_Course_Category_Db'),
        ),
        migrations.AddField(
            model_name='course_content_db',
            name='main_course_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Main_Course_Category_Db'),
        ),
        migrations.AddField(
            model_name='course_content_db',
            name='sub_course_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Sub_Course_Category_Db'),
        ),
        migrations.AddField(
            model_name='course_content_db',
            name='super_course_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ieltsapp.Super_Course_Category_Db'),
        ),
    ]