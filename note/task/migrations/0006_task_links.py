# Generated by Django 3.1.5 on 2021-05-14 11:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('task', '0005_auto_20210420_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=1000), blank=True,
                                                            null=True, size=None),
        ),
    ]
