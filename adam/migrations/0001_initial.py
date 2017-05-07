# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('prim_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('type', models.CharField(max_length=100, null=True)),
                ('terms', models.TextField(null=True)),
                ('query', models.TextField(null=True)),
                ('answer', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Questions',
            },
        ),
    ]