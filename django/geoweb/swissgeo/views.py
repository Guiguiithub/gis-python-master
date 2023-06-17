from django.shortcuts import render
from django.http import HttpResponse
from .models import Piste, Remontee, Batiment
from django.http import JsonResponse
from django.http import Http404
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db import connection


# Create your views here.
def index(request):
    return HttpResponse("Hi there this is Switzerland")


def list(request):
    remontees = Remontee.objects.order_by("rems_name")
    remontees_list = [model_to_dict(remontee) for remontee in remontees]
    pistes = Piste.objects.order_by("pistes_nam")
    pistes_list = [model_to_dict(piste) for piste in pistes]
    batiments = Batiment.objects.order_by("bat_name")
    batiments_list = [model_to_dict(batiment) for batiment in batiments]
    context = {'pistes': pistes_list,
               'remontees': remontees_list, 'batiments': batiments_list}
    return render(request, 'swissgeo/index.html', context)


def piste(request, id):
    try:
        pistes = Piste.objects.get(id=id)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ST_3DLength(ST_Transform(geom, 2056)) FROM public.pistes WHERE id= %s", [id])
        length = cursor.fetchall()
        if length:
            length = length[0][0]
        context = {
            'pistes': pistes,
            'length': length
        }
    except Piste.DoesNotExist:
        raise Http404("Piste pas trouvée")
    return render(request, 'swissgeo/piste.html', context)


def pistejson(request):
    piste = Piste.objects.all()
    ser = serialize('geojson', piste,
                    geometry_field='geom',
                    fields=('pistes_nam', 'type',))
    return HttpResponse(ser)


def getLengthPiste(request, name):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT ST_3DLength(ST_Transform(geom, 2056)) FROM public.pistes WHERE pistes_nam= %s", [name])
    length = cursor.fetchall()
    if length:
        length = length[0][0]

    length = int(length)

    return JsonResponse(length, safe=False)


def remonteejson(request):
    remontee = Remontee.objects.all()

    ser = serialize('geojson', remontee,
                    geometry_field='geom',
                    fields=('id', 'rems_name', 'type',))
    return HttpResponse(ser)


def remontee(request, id):
    try:
        remontees = Remontee.objects.get(id=id)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ST_3DLength(ST_Transform(geom, 2056)) FROM public.remontees WHERE id= %s", [id])
        length = cursor.fetchall()
        if length:
            length = length[0][0]
        context = {
            'remontees': remontees,
            'length': length
        }
    except Remontee.DoesNotExist:
        raise Http404("Remontée pas trouvée")
    return render(request, 'swissgeo/remontee.html', context)


def getLengthRemontee(request, name):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT ST_3DLength(ST_Transform(geom, 2056)) FROM public.remontees WHERE rems_name= %s", [name])
    length = cursor.fetchall()
    if length:
        length = length[0][0]

    length = int(length)

    return JsonResponse(length, safe=False)


def batimentjson(request):
    batiment = Batiment.objects.all()
    ser = serialize('geojson', batiment,
                    geometry_field='geom',
                    fields=('bat_name', 'type',))
    return HttpResponse(ser)


def batiment(request, id):
    try:
        batiments = Batiment.objects.get(id=id)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ST_Area(ST_Transform(geom, 2056)) FROM public.batiments WHERE id= %s", [id])
        area = cursor.fetchall()
        if area:
            area = area[0][0]
        context = {
            'batiments': batiments,
            'area': area
        }
    except Batiment.DoesNotExist:
        raise Http404("Batiment pas trouvée")
    return render(request, 'swissgeo/batiment.html', context)


def getAreaBatiment(request, name):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT ST_Area(ST_Transform(geom, 2056)) FROM public.batiments WHERE bat_name= %s", [name])

    length = cursor.fetchall()
    if length:
        length = length[0][0]

    length = int(length)

    return JsonResponse(length, safe=False)


def anzere(request):
    context = {}
    return render(request, 'swissgeo/anzere.html', context)
