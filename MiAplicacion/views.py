from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hola_mundo(request):
    return render(request,'hola_mundo.html')

def pagina(request):
    return render(request,'pagina.html')

def contacto(request):
    return render(request,'contacto.html')