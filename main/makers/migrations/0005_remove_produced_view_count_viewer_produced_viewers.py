# Generated by Django 4.1.7 on 2023-04-19 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('makers', '0004_alter_produced_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produced',
            name='view_count',
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='produced',
            name='viewers',
            field=models.ManyToManyField(to='makers.viewer'),
        ),
    ]
