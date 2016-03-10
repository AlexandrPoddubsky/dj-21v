# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 08:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=140)),
                ('gender', models.CharField(blank=True, max_length=140)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('website', models.URLField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='thumbpath')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
