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
    
def rechazar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.confirmar(producto)

    return redirect("vista_vendedor")

def limpiar(request):

    carrito = Carrito(request)
    carrito.limpiar()

    return redirect("carro")


def carro(request):

    return render(request, 'carro.html')

def vista_vendedor(request):

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()
    musicpro = {'productos': datos}

    return render(request, 'vista_vendedor.html', musicpro)

def vista_bodeguero(request):

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()
    musicpro = {'productos': datos}

    return render(request, 'vista_bodeguero.html', musicpro)

def vista_contador(request):

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()
    musicpro = {'productos': datos}

    return render(request, 'vista_contador.html', musicpro)

def login(request):

    return render(request, 'login.html')

def login_e(request):

    return render(request, 'login_e.html')
    
def registro(request):

    return render(request, 'registro.html')

def entrega(request):

    return render(request, 'entrega.html')

def pago(request):

    return render(request, 'pago.html')

def confirmar(request, producto_id):

    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.confirmar(producto)

    return redirect("vista_contador")
    
