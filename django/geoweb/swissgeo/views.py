from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Canton, Piste
from django.template import loader
from django.http import Http404
from django.core.serializers import serialize
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
    return HttpResponse("Hi there this is Switzerland")


def pistes(request):
    # output = ', '.join([c.city_name for c in top_cities])
    # return HttpResponse(output)
    pistes = Piste.objects.order_by("pistes_name")
    pistes_list = [model_to_dict(piste) for piste in pistes]
    context = {'pistes': pistes_list}
    return render(request, 'swissgeo/index.html', context)


def city(request, city_id):
    try:
        city = City.objects.get(pk=city_id)
    except City.DoesNotExist:
        raise Http404("City not found!!")
    return render(request, 'swissgeo/city.html', {'city': city})


def piste(request, id):
    try:
        pistes = Piste.objects.get(id=id)
        context = {
            'pistes': pistes
        }
    except Piste.DoesNotExist:
        raise Http404("Piste pas trouvée")
    return render(request, 'swissgeo/piste.html', context)


def cantonsjson(request):
    cantons = Canton.objects.all()
    ser = serialize('geojson', cantons,
                    geometry_field='geom',
                    fields=('name',))
    return HttpResponse(ser)


def cantons(request):
    context = {}
    return render(request,
                  'swissgeo/cantons.html', context)
