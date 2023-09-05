# Generated by Django 4.2.4 on 2023-08-28 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0001_initial'),
        ('subject', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, default='http://localhost:8000/static/images/profile.png', null=True, upload_to='profile_pics/')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('interests', models.CharField(blank=True, max_length=255, null=True)),
                ('memberships', models.CharField(blank=True, max_length=255, null=True)),
                ('awards', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(choices=[('Teacher', 'Teacher'), ('Instructor', 'Instructor'), ('Trainee', 'Trainee'), ('Staff', 'Staff')], default='Attorney', max_length=30)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, null=True)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('classes', models.ManyToManyField(blank=True, related_name='classroom', to='classroom.classroom')),
                ('subjects', models.ManyToManyField(blank=True, related_name='classroom', to='subject.subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]