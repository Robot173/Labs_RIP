# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horserace', '0007_auto_20170113_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='horse_picture',
            field=models.ImageField(blank=True, null=True, upload_to='/horserace/img/', verbose_name='Picture'),
        ),
    ]
