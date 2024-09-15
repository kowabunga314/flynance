from rest_framework import serializers

from aircraft.models import Aircraft, AircraftModel, Engine, Manufacturer


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


class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'
