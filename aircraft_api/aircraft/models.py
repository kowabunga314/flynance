from django.contrib.auth.models import User
from django.db import models


class ManufacturerCrawl(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Manufacturer(models.Model):
    """
    Manufacturer A manufacturer of aircraft, powerplants, or aftermarket mods and accessories.

    Args:
        models (_type_): _description_
    """
    AIRCRAFT_TYPE = ('aircraft', 'Aircraft')
    POWERPLANT_TYPE = ('powerplant', 'Powerplant')
    AFTERMARKET_TYPE = ('aftermarket', 'Aftermarket')
    MANUFACTURER_TYPES = sorted([
        AIRCRAFT_TYPE,
        POWERPLANT_TYPE,
        AFTERMARKET_TYPE
    ])
    name = models.CharField(max_length=200)
    manufacturer_type = models.CharField(max_length=32, choices=MANUFACTURER_TYPES)


class ModelCrawl(models.Model):
    manufacturer = models.ForeignKey(to=ManufacturerCrawl, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_parsed_at = models.DateTimeField(null=True, blank=True)

class AbstractAircraft(models.Model):
    FIXED_GEAR = ('fixed', 'Fixed')
    MANUAL_GEAR = ('manual', 'Manual')
    AUTO_GEAR = ('auto', 'Auto')
    FLOAT_GEAR = ('float', 'Float')
    SKI_GEAR = ('ski', 'Ski')
    SKID_GEAR = ('skid', 'Skid')
    OTHER_GEAR = ('other', 'Other')
    GEAR_TYPE_CHOICES = sorted([
        FIXED_GEAR,
        MANUAL_GEAR,
        AUTO_GEAR,
        FLOAT_GEAR,
        SKI_GEAR,
        SKID_GEAR,
        OTHER_GEAR
    ])
    MANUAL_FLAPS = ('manual', 'Manual')
    ELECTRIC_FLAPS = ('electric', 'Electric')
    OTHER_FLAPS = ('other', 'Other')
    NO_FLAPS = ('none', 'None')
    FLAP_TYPE_CHOICES = sorted([
        MANUAL_FLAPS,
        ELECTRIC_FLAPS,
        OTHER_FLAPS,
        NO_FLAPS
    ])
    DIGITAL_EM = ('digital', 'Digital')
    ANALOG_EM = ('analog', 'Analog')
    NO_EM = ('none', 'None')
    ENGINE_MONITOR_CHOICES = sorted([
        DIGITAL_EM,
        ANALOG_EM,
        NO_EM
    ])
    FIXED_PITCH = ('fixed_pitch', 'Fixed Pitch')
    CONSTANT_SPEED = ('constant_speed', 'Constant Speed')
    PROPELLER_TYPES = sorted([
        FIXED_PITCH,
        CONSTANT_SPEED
    ])
    gear_type = models.CharField(max_length=6, choices=GEAR_TYPE_CHOICES)
    flap_type = models.CharField(max_length=8, choices=FLAP_TYPE_CHOICES)
    propeller_type = models.CharField(max_length=24, choices=PROPELLER_TYPES, null=True)
    engine_monitor_type = models.CharField(max_length=7, choices=ENGINE_MONITOR_CHOICES, null=True)
    engine_count = models.IntegerField()
    total_cost_of_ownership = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    total_fixed_cost = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    total_variable_cost = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    annual_inspection_cost = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    fuel_burn = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    fuel_burn_cruise = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    fuel_capacity = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    fuel_unit = models.CharField(max_length=20, null=True)
    cruise_speed = models.IntegerField(null=True)
    stall_speed = models.IntegerField(null=True)
    ceiling = models.IntegerField(null=True)
    ceiling_engine_out = models.IntegerField(null=True)
    takeoff_distance = models.IntegerField(null=True)
    landing_distance = models.IntegerField(null=True)
    takeoff_distance_50 = models.IntegerField(null=True)
    landing_distance_50 = models.IntegerField(null=True)
    gross_weight = models.IntegerField(null=True)
    empty_weight = models.IntegerField(null=True)
    max_payload = models.IntegerField(null=True)
    range = models.IntegerField(null=True)
    rate_of_climb = models.IntegerField(null=True)
    rate_of_climb_engine_out = models.IntegerField(null=True)

    class Meta:
        abstract = True


class AircraftCrawl(models.Model):
    model_name = models.CharField(max_length=128, unique=True)
    engine_count = models.CharField(max_length=64, null=True, blank=True)
    total_cost_of_ownership = models.CharField(max_length=64, null=True, blank=True)
    total_fixed_cost = models.CharField(max_length=64, null=True, blank=True)
    total_variable_cost = models.CharField(max_length=64, null=True, blank=True)
    annual_inspection_cost = models.CharField(max_length=64, null=True, blank=True)
    fuel_burn = models.CharField(max_length=64, null=True, blank=True)
    fuel_burn_cruise = models.CharField(max_length=64, null=True, blank=True)
    fuel_capacity = models.CharField(max_length=64, null=True, blank=True)
    fuel_unit = models.CharField(max_length=64, null=True, blank=True)
    cruise_speed = models.CharField(max_length=64, null=True, blank=True)
    stall_speed = models.CharField(max_length=64, null=True, blank=True)
    ceiling = models.CharField(max_length=64, null=True, blank=True)
    ceiling_engine_out = models.CharField(max_length=64, null=True, blank=True)
    takeoff_distance = models.CharField(max_length=64, null=True, blank=True)
    landing_distance = models.CharField(max_length=64, null=True, blank=True)
    takeoff_distance_50 = models.CharField(max_length=64, null=True, blank=True)
    landing_distance_50 = models.CharField(max_length=64, null=True, blank=True)
    gross_weight = models.CharField(max_length=64, null=True, blank=True)
    empty_weight = models.CharField(max_length=64, null=True, blank=True)
    max_payload = models.CharField(max_length=64, null=True, blank=True)
    range = models.CharField(max_length=64, null=True, blank=True)
    rate_of_climb = models.CharField(max_length=64, null=True, blank=True)
    rate_of_climb_engine_out = models.CharField(max_length=64, null=True, blank=True)
    manufacturer = models.CharField(max_length=256, null=True, blank=True)
    engine = models.CharField(max_length=256, null=True, blank=True)
    owner = models.CharField(max_length=256, null=True, blank=True)
    unparsed_data = models.JSONField(default=dict)


# Create your models here.
class AircraftModel(AbstractAircraft):
    """
    AircraftModel This class represents a specific model type of an aircraft.

    The information from this table is used to inform users about a specific type of aircraft as well as populate data
        on an Aircraft when it is not provided during the create operation.
    """
    model_name = models.CharField(max_length=80)
    model_variant = models.CharField(max_length=80)
    engine_count = models.IntegerField()
    model_year_start = models.IntegerField(null=True)
    model_year_end = models.IntegerField(null=True)
    estimated_value = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    

    manufacturer = models.ForeignKey('ManufacturerCrawl', on_delete=models.PROTECT)
    engine = models.ForeignKey('Engine', on_delete=models.PROTECT, null=True)

    class Meta:
        unique_together = ('model_name', 'model_variant')


class AircraftListing(AbstractAircraft):
    """
    Aircraft This class represents a specific aircraft.

    An Aircraft instance is used to track a specific aircraft listing.

    Args:
        models (_type_): _description_
    """
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    listing_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    smoh = models.IntegerField(null=True)
    spoh = models.IntegerField(null=True)
    has_autopilot = models.BooleanField(null=True, default=False)
    has_complete_logs = models.BooleanField(null=True, default=False)
    has_damage_history = models.BooleanField(null=True, default=False)

    aircraft_model = models.ForeignKey('AircraftModel', on_delete=models.PROTECT)
    engine = models.ForeignKey('Engine', on_delete=models.PROTECT)


class Engine(models.Model):
    """
    Engine Summary of an engine model.

    Tracks specifications about a specific model of engine.

    Args:
        models (_type_): _description_
    """
    FUEL_INJECTED = ('fuel_injected', 'Fuel Injected')
    CARBURETED = ('carbureted', 'Carbureted')
    FUEL_DELIVERY_TYPES = sorted([
        FUEL_INJECTED,
        CARBURETED
    ])
    display_name = models.CharField(max_length=200)
    engine_family = models.CharField(max_length=64)
    engine_variant = models.CharField(max_length=64)
    cylinder_count = models.IntegerField()
    displacement = models.DecimalField(max_digits=4, decimal_places=2)
    fuel_delivery_type = models.CharField(max_length=20, choices=FUEL_DELIVERY_TYPES)
    recommended_tbo = models.IntegerField()
    turbocharger = models.BooleanField()
    supercharger = models.BooleanField()

    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT)
