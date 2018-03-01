# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-28 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortial_billing', '0034_referral_datetime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referral',
            options={'ordering': ('datetime',)},
        ),
        migrations.AddField(
            model_name='referral',
            name='referent_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='referral',
            name='referring_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]