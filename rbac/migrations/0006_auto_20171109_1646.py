# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_auto_20171109_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='menu_gp',
        ),
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='是否是菜单'),
            preserve_default=False,
        ),
    ]