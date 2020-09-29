# Generated by Django 3.1.1 on 2020-09-29 18:12

import customer.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('telephone', models.IntegerField(validators=[customer.validators.validate_phone_number])),
                ('has_purchase_history', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('purchase', models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('none', 'None')], default='none', max_length=250)),
            ],
            options={
                'unique_together': {('first_name', 'last_name', 'email')},
            },
        ),
    ]
