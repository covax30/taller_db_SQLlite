from django.shortcuts import render
from django .http import HttpResponse, JsonResponse

# Create your views here.
# ---------vistas karol------------------
def vista_administrador(request):
    return render(request, 'vista_admin.html')

def vista_informes(request):
    return render(request, 'vista_informes.html')

def vista_pago_servicios(request):
    return render(request, 'vista_pago_servicios.html')

def vista_proveedores(request):
    return render(request, 'vista_proveedores.html')

def vista_pagos(request):
    return render(request, 'vista_pagos.html')

def vista1(request):
    return HttpResponse('Hola esta es mi primera vista')

def vista2(request):
    persona = {
        'Nombre': 'Karol',
        'Apellido': 'Talero'
    }
    return JsonResponse(persona)
def vista3(request):
    return render(request, 'index.html')