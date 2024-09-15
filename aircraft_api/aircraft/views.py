from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from aircraft.models import Manufacturer, AircraftModel, Engine, Aircraft
from aircraft.serializers import ManufacturerSerializer, AircraftModelSerializer, EngineSerializer, AircraftSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class AircraftModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AircraftModel.objects.all()
    serializer_class = AircraftModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class EngineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    permission_classes = [permissions.IsAuthenticated]


class AircraftViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [permissions.IsAuthenticated]
