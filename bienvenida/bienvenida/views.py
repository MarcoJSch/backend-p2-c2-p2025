from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola mundo desde Django")

def mostrar_bievenida(request):
    name="Marco Jara"
    return HttpResponse(f"Bienvenidos a mi primera App Django, {name}!")

def que_pasa(request):
    return HttpResponse("que pasa")