# Generated by Django 4.0.3 on 2022-04-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0013_rename_input_id_machine_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_Status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], max_length=255, null=True),
        ),
    ]
