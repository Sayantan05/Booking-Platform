# Generated by Django 3.1.5 on 2021-03-06 06:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0003_business_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by',
                                    to='user.user'),
        ),
    ]
