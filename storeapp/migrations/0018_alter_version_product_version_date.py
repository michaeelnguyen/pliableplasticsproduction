# Generated by Django 4.0.3 on 2022-05-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0017_remove_version_product_product_version_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product_Version_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
