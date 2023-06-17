from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class Piste(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiLineStringField()
    pistes_nam = models.CharField(max_length=250)
    type = models.CharField(max_length=250, null=True)

    class Meta:
        db_table = "pistes"

    def __str__(self):
        return self.pistes_nam


class Remontee(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    geom = models.MultiLineStringField()
    rems_name = models.CharField(max_length=250)
    type = models.CharField(max_length=250, null=True)

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


class Batiment(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    bat_name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    geom = models.MultiPolygonField()

    class Meta:
        db_table = "batiments"

    def __str__(self):
        return self.bat_name


class PisteLength(models.Model):
    piste = models.OneToOneField(Piste, on_delete=models.CASCADE)
    tarnsformed_geom = models.MultiLineStringField()
    length = models.FloatField()

    def save(self, *args, **kwargs):
        transformed = self.piste.geom.transform(3857, clone=True)
        self.tarnsformed_geom = transformed
        self.length = transformed.length

        super().save(*args, **kwargs)

    class Meta:
        db_table = "piste_lengths"

    def __str__(self):
        return str(self.piste)
