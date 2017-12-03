# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-03 19:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171125_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='type',
            field=models.CharField(choices=[('1', 'Business company'), ('3', 'Law firm office')], default='2', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
        ),
    ]
