# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-12 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u8bfe\u7a0b',
                'proxy': True,
                'verbose_name_plural': '\u8f6e\u64ad\u8bfe\u7a0b',
            },
            bases=('courses.course',),
        ),
    ]