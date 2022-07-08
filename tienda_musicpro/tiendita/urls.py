from atexit import register
from django.urls import path, include, re_path
from .views import index, login, registro, tienda, carro, agregar, eliminar, restar, limpiar, sumar, vista_bodeguero, vista_contador, vista_vendedor
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('tienda/', tienda, name='tienda'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('vista_vendedor/', vista_vendedor, name='vista_vendedor'),
    path('vista_bodeguero/', vista_bodeguero, name='vista_bodeguero'),
    path('vista_contador/', vista_contador, name='vista_contador'),
    path('carro/', carro, name='carro'),
    path('agregar/<int:producto_id>/', agregar, name="Add"),
    path('sumar/<int:producto_id>/', sumar, name="Sum"),
    path('eliminar/<int:producto_id>/', eliminar, name="Del"),
    path('restar/<int:producto_id>/', restar, name="Sub"),
    path('limpiar/', limpiar, name="CLS"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
