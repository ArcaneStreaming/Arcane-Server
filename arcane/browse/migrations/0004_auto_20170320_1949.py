# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0003_auto_20170313_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
            ],
        ),
        migrations.AlterModelOptions(
            name='track',
            options={},
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='browse.Genre'),
        ),
    ]
