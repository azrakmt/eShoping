# Generated by Django 2.2 on 2021-08-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_products_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
