# Generated by Django 4.0.4 on 2022-05-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age2',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
