# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-22 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_ticket_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='author',
        ),
    ]
