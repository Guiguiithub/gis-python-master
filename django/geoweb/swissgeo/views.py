from django.shortcuts import render
from django.http import HttpResponse
from .models import Piste, Remontee
from django.template import loader
from django.http import Http404
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.contrib.gis.geos import GEOSGeometry


# Create your views here.
def index(request):
    return HttpResponse("Hi there this is Switzerland")


def pistes(request):
    # output = ', '.join([c.city_name for c in top_cities])
    # return HttpResponse(output)
    pistes = Piste.objects.order_by("pistes_nam")
    pistes_list = [model_to_dict(piste) for piste in pistes]
    context = {'pistes': pistes_list}
    return render(request, 'swissgeo/index.html', context)


def piste(request, id):
    try:
        pistes = Piste.objects.get(id=id)
        context = {
            'pistes': pistes
        }
    except Piste.DoesNotExist:
        raise Http404("Piste pas trouvée")
    return render(request, 'swissgeo/piste.html', context)


def pistejson(request):
    # remontee = Remontee.objects.all()
    piste = Piste.objects.all()
    # anzere = remontee.union(piste)
    ser = serialize('geojson', piste,
                    geometry_field='geom',
                    fields=('pistes_nam', 'type',))
    return HttpResponse(ser)


def remonteejson(request):
    remontee = Remontee.objects.all()
    ser = serialize('geojson', remontee,
                    geometry_field='geom',
                    fields=('rems_name', 'type',))
    return HttpResponse(ser)


def anzere(request):
    context = {}
    return render(request, 'swissgeo/anzere.html', context)


def cantons(request):
    context = {}
    return render(request,
                  'swissgeo/cantons.html', context)


def remontees(request):
    context = {}
    return render(request, 'swissgeo/')
