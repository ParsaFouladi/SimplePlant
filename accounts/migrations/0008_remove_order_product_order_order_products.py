# Generated by Django 4.0.4 on 2022-05-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_order_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_product',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='accounts.order_product'),
        ),
    ]
