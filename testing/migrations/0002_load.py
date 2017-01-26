# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ROWID', models.IntegerField(verbose_name=b'Row ID')),
                ('OrderID', models.IntegerField(verbose_name=b'Order ID')),
                ('OrderDate', models.CharField(max_length=30, verbose_name=b'Order Date')),
                ('OrderPri', models.CharField(max_length=30, verbose_name=b'Order Priority')),
                ('OrderQt', models.IntegerField(verbose_name=b'Order Quantity')),
                ('Sales', models.FloatField(verbose_name=b'Sales')),
                ('Disc', models.FloatField(verbose_name=b'Discount')),
                ('ShipMode', models.CharField(max_length=40, verbose_name=b'Ship Mode')),
                ('Profit', models.FloatField(verbose_name=b'Profit')),
                ('UnitPrice', models.FloatField(verbose_name=b'Unit Price')),
                ('Cost', models.FloatField(verbose_name=b'Ship Cost')),
                ('Name', models.CharField(max_length=100, verbose_name=b'Cust Name')),
                ('Province', models.CharField(max_length=100, verbose_name=b'Province')),
                ('Region', models.CharField(max_length=50, verbose_name=b'Region')),
                ('CustSeg', models.CharField(max_length=50, verbose_name=b'Cust Seg')),
                ('Category', models.CharField(max_length=100, verbose_name=b'Category')),
                ('SubCat', models.CharField(max_length=200, verbose_name=b'SubCat')),
                ('ProdName', models.CharField(max_length=1500, verbose_name=b'Product Name')),
                ('ProdCont', models.CharField(max_length=100, verbose_name=b'Product Container')),
                ('Margin', models.FloatField(verbose_name=b'Margin')),
                ('ShipDate', models.CharField(max_length=30, verbose_name=b'Order Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
