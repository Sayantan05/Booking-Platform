# Generated by Django 3.1.5 on 2021-01-09 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.usergroup'),
        ),
        migrations.AlterUniqueTogether(
            name='businesstimeslot',
            unique_together={('business', 'day')},
        ),
    ]
