# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horse_name', models.TextField(blank=True, max_length=20, null=True)),
                ('horse_owner', models.TextField(blank=True, max_length=80, null=True)),
                ('horse_club', models.TextField(blank=True, max_length=30, null=True)),
                ('horse_picture', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Picture')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
