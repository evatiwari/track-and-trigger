# Generated by Django 3.0.7 on 2020-11-27 19:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('u_id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric', regex='^[a-zA-Z0-9]*$')])),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phonenumber', message='Please enter a valid phone number', regex='^[0-9]*$')])),
                ('password', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(8)])),
                ('email', models.EmailField(max_length=254)),
                ('home', models.BooleanField(default=False, verbose_name='home status')),
                ('professional', models.BooleanField(default=False, verbose_name='pro status')),
            ],
        ),
    ]
