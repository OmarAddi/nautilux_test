# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-28 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intervention', '0002_intervention'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='date_crea',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='date_inter',
            field=models.DateTimeField(),
        ),
    ]
