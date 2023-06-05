from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('piste/', views.pistes, name='pistes'),
    path('city/<int:city_id>', views.city, name='city'),
    path('pistes/<int:id>', views.piste, name='piste'),
    path('cantons.json', views.cantonsjson, name='cantonsjson'),
    path('cantons', views.cantons, name='cantons'),
]
