from django.shortcuts import render
import requests

# Create your views here.
def index(request):   

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()

    musicpro = {'productos' : datos}

    return render(request,'index.html', musicpro)

def album(request):   

    url = 'http://127.0.0.1:8000/api/productos/'
    resp = requests.get(url, auth=('admin', 'tiendamusicpro'))
    datos = resp.json()

    musicpro = {'productos' : datos}

    return render(request,'album.html', musicpro)

def login(request):     
    return render(request,'contact.html')

