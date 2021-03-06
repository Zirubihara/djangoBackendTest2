# Generated by Django 3.1.1 on 2020-09-29 07:51

from django.db import migrations, models
import djangoBackendTest.customer.validators


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
                ('second_name', models.CharField(max_length=50)),
                ('telephone', models.IntegerField(validators=[djangoBackendTest.customer.validators.validate_phone_number])),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'unique_together': {('first_name', 'second_name', 'email')},
            },
        ),
    ]
