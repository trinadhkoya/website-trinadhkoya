# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-16 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.URLField(),
        ),
    ]
