from django.shortcuts import render

from produto.models import Produto


# Create your views here.
def inicio(request):
    return render(request,"home.html")

def historia(request):
    return render(request,"historia.html")

def home(request):
    return render(request,"home.html")

def salgadas(request, produtos=None):
    produtos = Produto.objects.all()
    return render(request,"pzsalgada.html", {'produtos': produtos})
