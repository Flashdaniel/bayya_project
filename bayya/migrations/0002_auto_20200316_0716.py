# Generated by Django 3.0.4 on 2020-03-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bayya', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
