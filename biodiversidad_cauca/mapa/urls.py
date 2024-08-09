from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import guardar_hostal, cargar_hostales, hostales_map, buscar_especies

urlpatterns = [
    path('', views.mapa_view, name='mapa'),
    path('guardar_ubicacion/', views.guardar_ubicacion, name='guardar_ubicacion'),
    path('guardar_hostal/', guardar_hostal, name='guardar_hostal'),
    path('hostales', hostales_map, name='hostales_map'),
    path('cargar-hostales/', cargar_hostales, name='cargar_hostales'),
    path('mapa_interactivo/', views.mapa_interactivo, name='mapa_interactivo'),
    path('buscar_especies/', buscar_especies, name='buscar_especies'),

]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)