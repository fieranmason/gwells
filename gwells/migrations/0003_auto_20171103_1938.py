# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-03 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0002_auto_20171103_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysubmission',
            name='intended_water_use',
            field=models.ForeignKey(blank=True, db_column='intended_water_use_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.IntendedWaterUse', verbose_name='Intended Water Use blog'),
        ),
    ]