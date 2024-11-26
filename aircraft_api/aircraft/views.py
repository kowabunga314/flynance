from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from aircraft.models import Manufacturer, AircraftModel, Engine, AircraftListing
from aircraft.serializers import (
    ManufacturerSerializer, AircraftModelSerializer, EngineSerializer, AircraftListingSerializer
)


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


class AircraftListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AircraftListing.objects.all()
    serializer_class = AircraftListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self):
        return self.queryset
