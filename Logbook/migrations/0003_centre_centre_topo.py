# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logbook', '0002_centre_centre_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='centre',
            name='centre_topo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
