# Generated by Django 4.0.4 on 2022-05-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]