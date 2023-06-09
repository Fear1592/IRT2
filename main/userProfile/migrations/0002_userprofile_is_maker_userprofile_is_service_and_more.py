# Generated by Django 4.1.7 on 2023-04-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_maker',
            field=models.BooleanField(default=False, verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_service',
            field=models.BooleanField(default=False, verbose_name='Услуги'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_shop',
            field=models.BooleanField(default=False, verbose_name='Онлайн магазин'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Модератор'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='Супер пользователь'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=30, verbose_name='Ник'),
        ),
    ]
