from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,"home.html")

def historia(request):
    return render(request,"historia.html")

def home(request):
    return render(request,"home.html")

def pzsalgada(request):
    return render(request,"pzsalgada.html")