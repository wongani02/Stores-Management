# Generated by Django 5.0.1 on 2024-02-01 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0002_tendernotice_stock_alter_procurementchoice_name'),
        ('stock', '0004_alter_product_web_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RFQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('closing_date', models.DateField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.product')),
            ],
        ),
        migrations.CreateModel(
            name='RFQbid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField()),
                ('sub_date', models.DateField(auto_now_add=True)),
                ('rfq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurement.rfq')),
            ],
        ),
    ]