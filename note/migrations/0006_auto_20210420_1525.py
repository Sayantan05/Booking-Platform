# Generated by Django 3.1.5 on 2021-04-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('note', '0005_auto_20210319_1313'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='note',
            name='unique-in-module',
        ),
        migrations.AddConstraint(
            model_name='note',
            constraint=models.UniqueConstraint(fields=('created_by', 'title', 'created_at'), name='unique-in-module'),
        ),
    ]
