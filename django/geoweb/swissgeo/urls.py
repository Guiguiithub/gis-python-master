from django.urls import path, re_path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('list', views.list, name='pistes'),
    path('pistes/<int:id>', views.piste, name='piste'),
    path('batiments/<int:id>', views.batiment, name='batiment'),
    path('remontees/<int:id>', views.remontee, name='remontee'),
    path('pistes.json', views.pistejson, name='pistejson'),
    path('remontee.json', views.remonteejson, name='remonteejson'),
    path('batiment.json', views.batimentjson, name='batimentjson'),
    path('anzere', views.anzere, name='anzere'),
    path('distance', views.distance, name='distance'),

    # path to get variables
    path('get_length_piste/<str:name>/',
         views.getLengthPiste, name='get_length_piste'),
    path('get_length_remontee/<str:name>/',
         views.getLengthRemontee, name='get_length_remontee'),
    path('get_area_batiment/<str:name>/',
         views.getAreaBatiment, name='get_area_batiment'),
    re_path(r'^closestPiste/(?P<lat>[-+]?[0-9]*\.?[0-9]+)/(?P<lng>[-+]?[0-9]*\.?[0-9]+)/$',
            views.closestPiste, name='closest_piste'),
    path('get_distance_piste/<str:name1>/<str:name2>/',
         views.getDistancePiste, name='get_distance_piste'),
]
