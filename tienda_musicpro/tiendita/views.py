from django.shortcuts import redirect, render
import requests
from tiendita.carrito import Carrito
from api.models import Producto

# Create your views here.


def index(request):

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()
    musicpro = {'productos': datos}

    return render(request,'index.html', musicpro)


def album(request):

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()
    musicpro = {'productos': datos}

    return render(request, 'album.html', musicpro)


def agregar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)

    return redirect("album")


def eliminar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)

    return redirect("album")

def restar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)

    return redirect("contact") 

def limpiar(request):

    carrito = Carrito(request)
    carrito.limpiar()

    return  redirect("contact") 


def login(request):

    return render(request, 'contact.html')
