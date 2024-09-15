from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from aircraft.views import AircraftViewSet, AircraftModelViewSet, EngineViewSet, ManufacturerViewSet

router = routers.DefaultRouter()
router.register(r'aircraft', AircraftViewSet)
router.register(r'aircraft-model', AircraftModelViewSet)
router.register(r'engine', EngineViewSet)
router.register(r'manufacturer', ManufacturerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
