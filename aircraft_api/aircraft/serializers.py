from rest_framework import serializers

from aircraft.models import AircraftListing, AircraftModel, Engine, Manufacturer


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
