# Generated by Django 3.1.1 on 2020-09-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20200929_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='purchaseXD',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
