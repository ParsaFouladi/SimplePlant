# Generated by Django 4.0.4 on 2022-05-28 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_bank_buyer_order_seller_shipping_company_transaction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
