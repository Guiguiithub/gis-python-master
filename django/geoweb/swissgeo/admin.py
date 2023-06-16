from django.contrib import admin
from django.contrib.gis import admin

from .models import Canton, Piste, Remontee, Batiment

# Register your models here.
admin.site.register(Remontee)
admin.site.register(Piste)
admin.site.register(Batiment)
admin.site.register(Canton, admin.OSMGeoAdmin)
