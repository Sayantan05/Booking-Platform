# Generated by Django 3.1.5 on 2021-05-20 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20210519_1600'),
        ('note', '0008_auto_20210519_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='task.task'),
        ),
    ]