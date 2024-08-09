from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Ubicacion, Habitat, Amenaza, Conservacion, Hostales, Especie
from django.conf import settings


def mapa_view(request):
    ubicaciones = Ubicacion.objects.all()
    habitats = Habitat.objects.all()
    amenazas = Amenaza.objects.all()
    conservaciones = Conservacion.objects.all()

    # Serializa las ubicaciones a JSON
    ubicaciones_json = serialize('json', ubicaciones, fields=('nombre', 'descripcion', 'latitud', 'longitud', 'imagen'))
    habitats_json = serialize('json', habitats, fields=('nombre', 'descripcion'))
    amenazas_json = serialize('json', amenazas, fields=('nombre', 'descripcion'))
    conservaciones_json = serialize('json', conservaciones, fields=('nombre', 'descripcion'))

    return render(request, 'mapa/mapa.html', {
        'ubicaciones': ubicaciones_json,
        'habitats': habitats_json,
        'amenazas': amenazas_json,
        'conservaciones': conservaciones_json,
        'MEDIA_URL': settings.MEDIA_URL,
    })


@csrf_exempt
def guardar_ubicacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')
        imagen = request.FILES.get('imagen')

        ubicacion = Ubicacion(
            nombre=nombre,
            descripcion=descripcion,
            latitud=latitud,
            longitud=longitud,
            imagen=imagen
        )
        ubicacion.save()

        return JsonResponse({
            'status': 'success',
            'id': ubicacion.id,
            'nombre': ubicacion.nombre,
            'descripcion': ubicacion.descripcion,
            'latitud': ubicacion.latitud,
            'longitud': ubicacion.longitud,
            'imagen': ubicacion.imagen.url if ubicacion.imagen else ''
        })

    return JsonResponse({'status': 'fail'})

def guardar_hostal(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')

        hostal = Hostales(
            nombreHostal=nombre,
            descripcionHostal=descripcion,
            latitudHostal=latitud,
            longitudHostal=longitud,
            precioHostal=precio,
            imagenHostal=imagen
        )
        hostal.save()

        return JsonResponse({
            'nombre': hostal.nombreHostal,
            'descripcion': hostal.descripcionHostal,
            'latitud': hostal.latitudHostal,
            'longitud': hostal.longitudHostal,
            'precio': hostal.precioHostal,
            'imagen': hostal.imagenHostal.url if hostal.imagenHostal else None
        })
    


def cargar_hostales(request):
    hostales = Hostales.objects.all().values(
        'nombreHostal', 'descripcionHostal', 'latitudHostal', 'longitudHostal', 'imagenHostal', 'precioHostal'
    )
    
    # Convertir las rutas de imagen a URLs completas
    hostales_con_imagenes = []
    for hostal in hostales:
        hostal_dict = dict(hostal)
        if hostal_dict['imagenHostal']:
            hostal_dict['imagenHostal'] = settings.MEDIA_URL + hostal_dict['imagenHostal']
        hostales_con_imagenes.append(hostal_dict)
    
    return JsonResponse(hostales_con_imagenes, safe=False)

def hostales_map(request):
    return render(request, 'hostales_map.html')

def mapa_interactivo(request):
    return render(request, 'mapa_interactivo.html')

def buscar_especies(request):
    query = request.GET.get('query', '')
    if query:
        especies = Especie.objects.filter(nombre__icontains=query).values('nombre', 'latitud', 'longitud')
    else:
        especies = []

    return JsonResponse(list(especies), safe=False)