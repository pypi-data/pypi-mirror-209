# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wellsfargo", "0003_auto_20170510_1633"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountinquiryresult",
            name="middle_initial",
            field=models.CharField(
                blank=True, max_length=1, null=True, verbose_name="Middle Initial"
            ),
        ),
    ]
