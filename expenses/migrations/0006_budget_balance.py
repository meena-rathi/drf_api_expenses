# Generated by Django 4.2 on 2024-09-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_remove_budget_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
