# Generated by Django 5.1.1 on 2024-11-29 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0007_aircraftcrawl_unparsed_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraftcrawl',
            name='engine_monitor_type',
        ),
        migrations.RemoveField(
            model_name='aircraftcrawl',
            name='flap_type',
        ),
        migrations.RemoveField(
            model_name='aircraftcrawl',
            name='gear_type',
        ),
        migrations.RemoveField(
            model_name='aircraftcrawl',
            name='propeller_type',
        ),
    ]