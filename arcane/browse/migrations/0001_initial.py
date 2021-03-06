# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 19:03
from __future__ import unicode_literals

import arcane.browse.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artwork', models.ImageField(blank=True, null=True, upload_to=arcane.browse.models.upload_album_artwork)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to=arcane.browse.models.upload_artist_photo)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(default='#D50000', max_length=7)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=arcane.browse.models.upload_genre_icon)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_count', models.BigIntegerField(default=0)),
                ('url', models.FileField(blank=True, null=True, upload_to=arcane.browse.models.upload_track)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('duration', models.CharField(blank=True, max_length=200)),
                ('length', models.BigIntegerField(blank=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Album')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Artist')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Genre'),
        ),
    ]
