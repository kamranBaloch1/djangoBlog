# Generated by Django 4.0.5 on 2022-06-26 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]