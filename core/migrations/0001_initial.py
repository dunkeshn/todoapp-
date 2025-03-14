# Generated by Django 5.0.7 on 2024-08-20 13:43

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Никнейм')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='Почта')),
                ('about', models.TextField(blank=True, verbose_name='О себе')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('picture', models.ImageField(blank=True, default='pictures/default.jpg', null=True, upload_to='pictures', verbose_name='Фото')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('friends', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Друзья')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['email'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('priority', models.CharField(choices=[('COMMON', 'Обычный'), ('LOW', 'Низкий'), ('MEDIUM', 'Средний'), ('HIGH', 'Высокий')], default='COMMON', max_length=50, verbose_name='Приоритет')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('owners', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['created_at'],
            },
        ),
    ]
