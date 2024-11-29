from decimal import Decimal
from pprint import pprint
from pydantic import BaseModel, Field
from rest_framework import serializers
from typing import ClassVar, Optional

from aircraft.models import AircraftListing, AircraftModel, Engine, Manufacturer, AircraftCrawl


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class EngineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class AircraftModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AircraftModel
        fields = '__all__'


class AircraftListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AircraftListing
        fields = '__all__'


class AircraftCrawlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftCrawl
        fields = '__all__'


class AircraftCrawlNormalizer(BaseModel):
    gear_type: Optional[str] = Field(max_length=24)
    flap_type: Optional[str] = Field(max_length=24)
    propeller_type: Optional[str] = Field(max_length=24)
    engine_monitor_type: Optional[str] = Field(max_length=24)
    engine_count: Optional[int] = Field(ge=0)
    total_cost_of_ownership: Optional[Decimal] = Field(max_digits=9, decimal_places=2)
    total_fixed_cost: Optional[Decimal] = Field(max_digits=9, decimal_places=2)
    total_variable_cost: Optional[Decimal] = Field(max_digits=9, decimal_places=2)
    annual_inspection_cost: Optional[Decimal] = Field(max_digits=9, decimal_places=2)
    fuel_burn: Optional[Decimal] = Field(max_digits=6, decimal_places=2)
    fuel_burn_cruise: Optional[Decimal] = Field(max_digits=6, decimal_places=2)
    fuel_capacity: Optional[Decimal] = Field(max_digits=6, decimal_places=2)
    fuel_unit: Optional[str] = Field(max_length=24)
    cruise_speed: Optional[int] = Field(ge=0)
    stall_speed: Optional[int] = Field(ge=0)
    ceiling: Optional[int] = Field(ge=0)
    ceiling_engine_out: Optional[int] = Field(ge=0)
    takeoff_distance: Optional[int] = Field(ge=0)
    landing_distance: Optional[int] = Field(ge=0)
    takeoff_distance_50: Optional[int] = Field(ge=0)
    landing_distance_50: Optional[int] = Field(ge=0)
    gross_weight: Optional[int] = Field(ge=0)
    empty_weight: Optional[int] = Field(ge=0)
    max_payload: Optional[int] = Field(ge=0)
    range: Optional[int] = Field(ge=0)
    rate_of_climb: Optional[int] = Field(ge=0)
    rate_of_climb_engine_out: Optional[int] = Field(ge=0)

    def map_inputs(self, data):
        # Create a new dictionary with the mapped keys
        mapped_data = {}
        for key, value in data.items():
            # print(f'Handling key {key} and value {value}')
            # print(f'Key in mapped data: {key in list(self.FIELD_NAME_MAPPING.keys())}')
            # Use the mapping to transform field names
            mapped_key = self.FIELD_NAME_MAPPING.get(key, key)  # Default to the original key if not in mapping
            mapped_data[mapped_key] = value


class AircraftDataMapper():
    data: dict = None
    unrecognized_fields: dict = None
    FIELD_NAME_MAPPING = {
        'Annual inspection cost': 'annual_inspection_cost',
        'Best Cruise Speed': 'cruise_speed',
        'Best Range (i)': 'range',
        'Ceiling': 'ceiling',
        'Empty Weight': 'empty_weight',
        'Fuel Burn @ 75%': 'fuel_burn_cruise',
        'Fuel capacity': 'fuel_capacity',
        'Gross Weight': 'gross_weight',
        'Landing distance': 'landing_distance',
        'Landing distance over 50ft obstacle': 'landing_distance_50',
        'Rate of climb': 'rate_of_climb',
        'Stall Speed': 'stall_speed',
        'Takeoff distance': 'takeoff_distance',
        'Takeoff distance over 50ft obstacle': 'takeoff_distance_50',
        'Model': 'engine',
    }

    def __init__(self, data):
        self.data = data

    def get_normalized_data(self):
        self.data = self._map_inputs()
        return self.data


    def _map_inputs(self):
        # Create a new dictionary with the mapped keys
        mapped_data = {}
        unrecognized_fields = {}
        for key, value in self.data.items():
            print(f'Handling key {key} and value {value}')
            # print(f'Key in mapped data: {key in list(self.FIELD_NAME_MAPPING.keys())}')
            # Use the mapping to transform field names
            mapped_key = self.FIELD_NAME_MAPPING.get(key)  # Default to the original key if not in mapping
            if mapped_key is not None:
                mapped_data[mapped_key] = value
            else:
                unrecognized_fields[key] = value
        mapped_data['unparsed_data'] = unrecognized_fields
        return mapped_data