# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horserace', '0004_auto_20170113_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='horse_picture',
            field=models.ImageField(blank=True, null=True, upload_to='/static/img/', verbose_name='Picture'),
        ),
    ]
