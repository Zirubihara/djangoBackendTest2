# Generated by Django 3.1.1 on 2020-09-29 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200929_0958'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together={('first_name', 'second_name', 'email')},
        ),
    ]
