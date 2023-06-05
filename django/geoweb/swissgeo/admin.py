from django.contrib import admin
from django.contrib.gis import admin

from .models import City, Canton, Piste

# Register your models here.
admin.site.register(City)
admin.site.register(Piste)
admin.site.register(Canton, admin.OSMGeoAdmin)
