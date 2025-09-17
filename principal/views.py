from django.shortcuts import render
from categoria.models import Categoria
from produto.models import Produto


# Create your views here.
def inicio(request):
    return render(request,"home.html")

def historia(request):
    return render(request,"historia.html")

def home(request):
    return render(request,"home.html")

def salgadas(request):
    salgadas = Categoria.objects.get(nome='Pizza Salgada')
    produtos = Produto.objects.filter(categoria=salgadas)
    return render(request, "pzsalgada.html", {'produtos': produtos})


def doce(request):
    doce = Categoria.objects.get(nome='Pizza Doce')
    produtos = Produto.objects.filter(categoria=doce)
    return render(request, "pzdoce.html", {'produtos': produtos})
