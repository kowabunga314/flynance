# Generated by Django 5.1.1 on 2024-11-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0008_remove_aircraftcrawl_engine_monitor_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraftcrawl',
            name='model_name',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]