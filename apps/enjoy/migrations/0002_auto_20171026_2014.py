# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 20:14
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enjoy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enjoyinfo',
            name='enjoy_info',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', help_text='客片故事', null=True, verbose_name='客片故事'),
        ),
    ]