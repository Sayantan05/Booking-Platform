# Generated by Django 3.1.5 on 2021-03-19 12:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0002_auto_20210310_0917'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('title', 'created_by')},
        ),
    ]
