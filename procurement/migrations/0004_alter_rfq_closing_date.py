# Generated by Django 5.0.1 on 2024-02-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0003_rfq_budget_rfq_safety_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfq',
            name='closing_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
