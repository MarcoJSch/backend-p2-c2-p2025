from django.http import HttpResponse
from .models import Producto
from django.shortcuts import render

def inicio(request):
    return HttpResponse("Hola mundo desde Django")

def mostrar_bievenida(request):
    name="Marco Jara"
    return HttpResponse(f"Bienvenidos a mi primera App Django, {name}!")

def que_pasa(request):
    return HttpResponse("que pasa")

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})