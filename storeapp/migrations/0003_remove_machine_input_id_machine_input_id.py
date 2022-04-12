# Generated by Django 4.0.3 on 2022-04-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_remove_machine_input_id_machine_input_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='input_ID',
        ),
        migrations.AddField(
            model_name='machine',
            name='input_ID',
            field=models.ManyToManyField(to='storeapp.inputitem'),
        ),
    ]
