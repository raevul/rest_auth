# Generated by Django 4.0.4 on 2022-05-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
