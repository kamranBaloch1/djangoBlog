# Generated by Django 4.0.5 on 2022-06-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='what is the slug', max_length=200),
        ),
    ]
