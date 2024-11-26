from django.contrib import admin
from aircraft.models import AircraftListing, AircraftModel, Engine, Manufacturer, ManufacturerCrawl, ModelCrawl


# Register your models here.
admin.site.register(AircraftListing)
admin.site.register(AircraftModel)
admin.site.register(Engine)
admin.site.register(Manufacturer)
admin.site.register(ManufacturerCrawl)
admin.site.register(ModelCrawl)