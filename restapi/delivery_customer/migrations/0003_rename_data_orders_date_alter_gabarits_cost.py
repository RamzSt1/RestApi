# Generated by Django 4.1.3 on 2023-03-10 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_customer', '0002_orders_customer_orders_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='gabarits',
            name='cost',
            field=models.FloatField(),
        ),
    ]
