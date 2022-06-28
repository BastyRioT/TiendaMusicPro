from django.shortcuts import redirect, render
import requests
from tiendita.carrito import Carrito
from api.models import Producto

# Create your views here.


def index(request):

    return render(request, 'index.html')


def tienda(request):

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()
    musicpro = {'productos': datos}

    return render(request, 'tienda.html', musicpro)


def agregar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)

    return redirect("tienda")


def eliminar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)

    return redirect("tienda")


def sumar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)

    return redirect("carro")


def restar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)

    return redirect("carro")


def limpiar(request):

    carrito = Carrito(request)
    carrito.limpiar()

    return redirect("carro")


def carro(request):

    return render(request, 'carro.html')
