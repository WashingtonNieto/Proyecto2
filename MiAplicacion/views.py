from django.shortcuts import render

# Create your views here.
def index(request):

    nombre='Washington Nieto'
    lenguajes = ['JavaScript','Python','PHP','c']

    return render(request, 'index.html', {
        'mi_variable':'Soy un dato que está en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
    })

def hola_mundo(request):
    return render(request,'hola_mundo.html')

def pagina(request):
    return render(request,'pagina.html')

def contacto(request):
    return render(request,'contacto.html')