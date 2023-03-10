# Generated by Django 3.2.16 on 2022-12-20 00:49

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('student_rating', models.IntegerField(default=0)),
                ('language', models.CharField(max_length=225)),
                ('course_length', models.CharField(default=0, max_length=20)),
                ('course_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('image_url', models.ImageField(upload_to='course_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('file', models.FileField(upload_to='course_videos')),
                ('length', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('sector_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('sector_image', models.ImageField(upload_to='sector_images')),
                ('related_courses', models.ManyToManyField(blank=True, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(blank=True, max_length=225, null=True)),
                ('section_number', models.IntegerField(blank=True, null=True)),
                ('episodes', models.ManyToManyField(blank=True, to='courses.Episode')),
            ],
        ),
    ]
