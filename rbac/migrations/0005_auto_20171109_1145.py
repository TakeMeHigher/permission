# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20171108_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='is_menu',
        ),
        migrations.AddField(
            model_name='permission',
            name='menu_gp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Permission', verbose_name='组内菜单'),
        ),
    ]
