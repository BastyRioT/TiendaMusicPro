from django.shortcuts import render

# Create your views here.
def index(request):     
    return render(request,'index.html')

def album(request):     
    return render(request,'album.html')

def login(request):     
    return render(request,'contact.html')