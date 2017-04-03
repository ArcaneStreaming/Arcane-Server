# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 21:41
from __future__ import unicode_literals

import arcane.users.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('browse', '0003_auto_20170313_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=124)),
                ('password', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tracks', models.ManyToManyField(to='browse.Track')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('DARK', 'ARCANE_DARK'), ('LIGH', 'ARCANE_LIGHT'), ('PAND', 'PANDORA'), ('SPOT', 'SPOTIFY'), ('PLAY', 'GOOGLE_PLAY'), ('CUST', 'CUSTOM')], default='DARK', max_length=4)),
                ('player_pos', models.CharField(choices=[('RIGH', 'RIGHT DRAWER'), ('LEFT', 'LEFT DRAWER'), ('HEAD', 'HEADER'), ('FOOT', 'FOOTER')], default='RIGH', max_length=4)),
                ('allow_explicit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(default='USA', max_length=3)),
                ('avatar', models.ImageField(blank=True, height_field=124, null=True, upload_to=arcane.users.models.upload_user_avatar, width_field=124)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Artist')),
                ('settings', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Settings')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]