# Generated by Django 4.1.7 on 2023-04-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makers', '0007_remove_viewer_ipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='produced',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Колличество просмотров'),
        ),
    ]