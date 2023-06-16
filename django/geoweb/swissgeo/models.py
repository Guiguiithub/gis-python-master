from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class Piste(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiLineStringField()
    pistes_name = models.CharField(max_length=250)

    class Meta:
        db_table = "pistes"

    def __str__(self):
        return self.pistes_name


class Remontee(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiLineStringField()
    rems_name = models.CharField(max_length=250)

    class Meta:
        db_table = "remontees"

    def __str__(self):
        return self.rems_name


class Canton(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    geom = models.MultiPolygonField(srid=4326, null=True)

    class Meta:
        db_table = "cantons"

    def __str__(self):
        return self.name
