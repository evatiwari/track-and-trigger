# Generated by Django 3.0.7 on 2020-11-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('quantity', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=150)),
            ],
        ),
    ]
