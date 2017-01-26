# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_auto_20170111_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='Cost',
            field=models.CharField(max_length=30, verbose_name=b'Ship Cost'),
        ),
        migrations.AlterField(
            model_name='load',
            name='Disc',
            field=models.CharField(max_length=30, verbose_name=b'Discount'),
        ),
        migrations.AlterField(
            model_name='load',
            name='Margin',
            field=models.CharField(max_length=30, verbose_name=b'Margin'),
        ),
        migrations.AlterField(
            model_name='load',
            name='Profit',
            field=models.CharField(max_length=30, verbose_name=b'Profit'),
        ),
        migrations.AlterField(
            model_name='load',
            name='Sales',
            field=models.CharField(max_length=30, verbose_name=b'Sales'),
        ),
        migrations.AlterField(
            model_name='load',
            name='UnitPrice',
            field=models.CharField(max_length=30, verbose_name=b'Unit Price'),
        ),
    ]
