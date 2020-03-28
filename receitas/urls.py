from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita', views.receita, name='receita'),
    path('bolo_cenoura', views.bolo_cenoura, name='bolo_cenoura'),
    path('bolo_chocolate', views.bolo_chocolate, name='bolo_chocolate'),
    path('torta_maca', views.torta_maca, name='torta_maca')
]
