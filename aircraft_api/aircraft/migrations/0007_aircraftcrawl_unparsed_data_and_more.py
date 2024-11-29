# Generated by Django 5.1.1 on 2024-11-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0006_aircraftcrawl'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraftcrawl',
            name='unparsed_data',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='annual_inspection_cost',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='ceiling',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='ceiling_engine_out',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='cruise_speed',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='empty_weight',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='engine_count',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='fuel_burn',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='fuel_burn_cruise',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='fuel_capacity',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='fuel_unit',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='gross_weight',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='landing_distance',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='landing_distance_50',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='max_payload',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='range',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='rate_of_climb',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='rate_of_climb_engine_out',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='stall_speed',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='takeoff_distance',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='takeoff_distance_50',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='total_cost_of_ownership',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='total_fixed_cost',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='aircraftcrawl',
            name='total_variable_cost',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]