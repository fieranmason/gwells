# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-03 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0003_auto_20171103_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysubmission',
            name='intended_water_use',
            field=models.ForeignKey(blank=True, db_column='intended_water_use_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.IntendedWaterUse', verbose_name='MMMIntended Water Use'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='well_subclass',
            field=models.ForeignKey(blank=True, db_column='well_subclass_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.WellSubclass', verbose_name='Well Subclass MMM'),
        ),
    ]