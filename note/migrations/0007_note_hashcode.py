# Generated by Django 3.1.5 on 2021-05-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('note', '0006_auto_20210420_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='hashcode',
            field=models.CharField(default='0000', max_length=1000),
        ),
    ]