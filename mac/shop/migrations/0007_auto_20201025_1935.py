# Generated by Django 3.0.10 on 2020-10-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
