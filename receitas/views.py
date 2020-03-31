from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
	data = {
		'recipes_names': [
			'Bolo de Cenoura', 
			'Bolo de Chocolate',
			'Torta de Maça'
		]
	}
	return render(request=request, template_name='index.html', context=data)


def receita(request):
	return render(request=request, template_name='receita.html')


def bolo_cenoura(request):
	return render(request=request, template_name='bolo_cenoura.html')


def bolo_chocolate(request):
	return render(request=request, template_name='bolo_chocolate.html')


def torta_maca(request):
	return render(request=request, template_name='torta_maca.html')