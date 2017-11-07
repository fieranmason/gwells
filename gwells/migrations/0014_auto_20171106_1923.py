# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-06 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0013_intakemethod_status_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreenIntakeMethod',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30, null=True)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_intake_method_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('screen_intake_code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('status_flag', models.BooleanField(choices=[(False, 'N'), (True, 'Y')], default=False)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['sort_order', 'description'],
                'db_table': 'gwells_screen_intake_method',
            },
        ),
        migrations.RemoveField(
            model_name='well',
            name='intake_method',
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='intake_method',
            field=models.ForeignKey(blank=True, db_column='screen_intake_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenIntakeMethod', verbose_name='Intake'),
        ),
        migrations.DeleteModel(
            name='IntakeMethod',
        ),
        migrations.AddField(
            model_name='well',
            name='screen_intake_method',
            field=models.ForeignKey(blank=True, db_column='screen_intake_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenIntakeMethod', verbose_name='Screen Intake Method'),
        ),
    ]