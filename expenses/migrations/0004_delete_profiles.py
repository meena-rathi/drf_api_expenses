# Generated by Django 4.2 on 2024-09-05 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_profiles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]
