# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-05-13 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0006_auto_20200513_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricehistory',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
