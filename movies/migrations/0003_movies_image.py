# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-16 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, default='groups/photos/joker.png', upload_to='movies/photos'),
        ),
    ]
