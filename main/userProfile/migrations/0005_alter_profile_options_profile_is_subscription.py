# Generated by Django 4.1.7 on 2023-04-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_profile_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['id'], 'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
        migrations.AddField(
            model_name='profile',
            name='is_subscription',
            field=models.BooleanField(default=False, verbose_name='Активонсть подписки'),
        ),
    ]