# Generated by Django 5.0.8 on 2024-09-28 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_restaurant_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='user',
        ),
    ]
