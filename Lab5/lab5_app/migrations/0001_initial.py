# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True
    database = 'first_db'
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('bet_id', models.AutoField(primary_key=True, serialize=False)),
                ('bet_price', models.IntegerField()),
                ('bet_multiplier', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('horse_id', models.AutoField(primary_key=True, serialize=False)),
                ('horse_name', models.TextField(max_length=20)),
                ('horse_owner', models.TextField(max_length=80)),
                ('horse_club', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('last_name', models.TextField(max_length=30)),
                ('first_name', models.TextField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='bet_horse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab5_app.Horse'),
        ),
        migrations.AddField(
            model_name='bet',
            name='bet_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab5_app.User'),
        ),
    ]
