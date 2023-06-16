from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('pistes', views.pistes, name='pistes'),
    path('pistes/<int:id>', views.piste, name='piste'),
    path('pistes.json', views.pistejson, name='pistejson'),
    path('remontee.json', views.remonteejson, name='remonteejson'),
    path('anzere', views.anzere, name='anzere'),
]
