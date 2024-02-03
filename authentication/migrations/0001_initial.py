# Generated by Django 5.0.1 on 2024-01-22 16:47

import authentication.models
import django.db.models.deletion
import enumchoicefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('permissions', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.CharField(blank=True, max_length=200, null=True)),
                ('faculty', enumchoicefield.fields.EnumChoiceField(blank=True, default=authentication.models.Faculties(7), enum_class=authentication.models.Faculties, max_length=8, null=True)),
                ('course', models.IntegerField(blank=True, default=1, null=True)),
                ('group', models.IntegerField(blank=True, default=1, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telegram', models.CharField(blank=True, max_length=100, null=True)),
                ('login', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='roles', to='authentication.role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]