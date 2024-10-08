# Generated by Django 5.1.1 on 2024-09-15 18:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=200)),
                ('engine_family', models.CharField(max_length=64)),
                ('engine_variant', models.CharField(max_length=64)),
                ('cylinder_count', models.IntegerField()),
                ('displacement', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fuel_delivery_type', models.CharField(choices=[('carbureted', 'Carbureted'), ('fuel_injected', 'Fuel Injected')], max_length=20)),
                ('recommended_tbo', models.IntegerField()),
                ('turbocharger', models.BooleanField()),
                ('supercharger', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer_type', models.CharField(choices=[('aftermarket', 'Aftermarket'), ('aircraft', 'Aircraft'), ('powerplant', 'Powerplant')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='AircraftModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear_type', models.CharField(choices=[('auto', 'Auto'), ('fixed', 'Fixed'), ('float', 'Float'), ('manual', 'Manual'), ('other', 'Other'), ('ski', 'Ski'), ('skid', 'Skid')], max_length=6)),
                ('flap_type', models.CharField(choices=[('electric', 'Electric'), ('manual', 'Manual'), ('none', 'None'), ('other', 'Other')], max_length=8)),
                ('propeller_type', models.CharField(choices=[('constant_speed', 'Constant Speed'), ('fixed_pitch', 'Fixed Pitch')], max_length=24, null=True)),
                ('engine_monitor_type', models.CharField(choices=[('analog', 'Analog'), ('digital', 'Digital'), ('none', 'None')], max_length=7, null=True)),
                ('total_cost_of_ownership', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('total_fixed_cost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('total_variable_cost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('annual_inspection_cost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('fuel_burn', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('fuel_burn_cruise', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('fuel_capacity', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('fuel_unit', models.CharField(max_length=20, null=True)),
                ('cruise_speed', models.IntegerField(null=True)),
                ('stall_speed', models.IntegerField(null=True)),
                ('ceiling', models.IntegerField(null=True)),
                ('ceiling_engine_out', models.IntegerField(null=True)),
                ('takeoff_distance', models.IntegerField(null=True)),
                ('landing_distance', models.IntegerField(null=True)),
                ('takeoff_distance_50', models.IntegerField(null=True)),
                ('landing_distance_50', models.IntegerField(null=True)),
                ('gross_weight', models.IntegerField(null=True)),
                ('empty_weight', models.IntegerField(null=True)),
                ('max_payload', models.IntegerField(null=True)),
                ('range', models.IntegerField(null=True)),
                ('rate_of_climb', models.IntegerField(null=True)),
                ('rate_of_climb_engine_out', models.IntegerField(null=True)),
                ('model_name', models.CharField(max_length=80)),
                ('model_variant', models.CharField(max_length=80)),
                ('engine_count', models.IntegerField()),
                ('model_year_start', models.IntegerField(null=True)),
                ('model_year_end', models.IntegerField(null=True)),
                ('estimated_value', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aircraft.engine')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aircraft.manufacturer')),
            ],
            options={
                'unique_together': {('model_name', 'model_variant')},
            },
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear_type', models.CharField(choices=[('auto', 'Auto'), ('fixed', 'Fixed'), ('float', 'Float'), ('manual', 'Manual'), ('other', 'Other'), ('ski', 'Ski'), ('skid', 'Skid')], max_length=6)),
                ('flap_type', models.CharField(choices=[('electric', 'Electric'), ('manual', 'Manual'), ('none', 'None'), ('other', 'Other')], max_length=8)),
                ('propeller_type', models.CharField(choices=[('constant_speed', 'Constant Speed'), ('fixed_pitch', 'Fixed Pitch')], max_length=24, null=True)),
                ('engine_monitor_type', models.CharField(choices=[('analog', 'Analog'), ('digital', 'Digital'), ('none', 'None')], max_length=7, null=True)),
                ('engine_count', models.IntegerField()),
                ('total_cost_of_ownership', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('total_fixed_cost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('total_variable_cost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('annual_inspection_cost', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('fuel_burn', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('fuel_burn_cruise', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('fuel_capacity', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('fuel_unit', models.CharField(max_length=20, null=True)),
                ('cruise_speed', models.IntegerField(null=True)),
                ('stall_speed', models.IntegerField(null=True)),
                ('ceiling', models.IntegerField(null=True)),
                ('ceiling_engine_out', models.IntegerField(null=True)),
                ('takeoff_distance', models.IntegerField(null=True)),
                ('landing_distance', models.IntegerField(null=True)),
                ('takeoff_distance_50', models.IntegerField(null=True)),
                ('landing_distance_50', models.IntegerField(null=True)),
                ('gross_weight', models.IntegerField(null=True)),
                ('empty_weight', models.IntegerField(null=True)),
                ('max_payload', models.IntegerField(null=True)),
                ('range', models.IntegerField(null=True)),
                ('rate_of_climb', models.IntegerField(null=True)),
                ('rate_of_climb_engine_out', models.IntegerField(null=True)),
                ('listing_url', models.URLField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('smoh', models.IntegerField(null=True)),
                ('spoh', models.IntegerField(null=True)),
                ('has_autopilot', models.BooleanField(default=False, null=True)),
                ('has_complete_logs', models.BooleanField(default=False, null=True)),
                ('has_damage_history', models.BooleanField(default=False, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('aircraft_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aircraft.aircraftmodel')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aircraft.engine')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='engine',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aircraft.manufacturer'),
        ),
    ]
