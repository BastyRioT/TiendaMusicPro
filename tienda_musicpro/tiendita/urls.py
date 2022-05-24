from django.urls import path, include, re_path
from .views import index, album, login, agregar, eliminar, restar, limpiar
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
   path('', index, name='index'),
   path('album/', album, name='album'),
   path('contact/', login, name='contact'),
   path('agregar/<int:producto_id>/', agregar, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar, name="Del"),
    path('restar/<int:producto_id>/', restar, name="Sub"),
    path('limpiar/', limpiar, name="CLS"),
    
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)