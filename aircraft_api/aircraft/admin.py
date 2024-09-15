from django.contrib import admin
from aircraft.models import Aircraft, AircraftModel, Engine, Manufacturer


# Register your models here.
admin.site.register(Aircraft)
admin.site.register(AircraftModel)
admin.site.register(Engine)
admin.site.register(Manufacturer)