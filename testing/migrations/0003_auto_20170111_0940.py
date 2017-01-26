# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_load'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='ProdName',
            field=models.TextField(max_length=1500, verbose_name=b'Product Name'),
        ),
    ]
