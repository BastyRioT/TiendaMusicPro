from django.urls import path,include,re_path
from .views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
   path('',index, name='index'),
    
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)