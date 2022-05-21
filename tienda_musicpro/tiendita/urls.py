from django.urls import path, include, re_path
from .views import index, album, login
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
   path('', index, name='index'),
   path('album/', album, name='album'),
   path('contact/', login, name='contact'),
    
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)