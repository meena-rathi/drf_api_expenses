# Generated by Django 4.2 on 2024-09-06 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_delete_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='balance',
        ),
    ]
