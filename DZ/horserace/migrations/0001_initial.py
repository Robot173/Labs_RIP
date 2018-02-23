# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 17:54
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
                ('horse_name', models.TextField(max_length=20)),
                ('horse_owner', models.TextField(max_length=80)),
                ('horse_club', models.TextField(max_length=30, null=True)),
                ('horse_picture', models.ImageField(height_field=100, upload_to='images/', verbose_name='Picture', width_field=100)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]