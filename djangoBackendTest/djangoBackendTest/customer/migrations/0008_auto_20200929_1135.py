# Generated by Django 3.1.1 on 2020-09-29 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20200929_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='purchaseXD',
            new_name='purchase',
        ),
    ]