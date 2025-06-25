from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.
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