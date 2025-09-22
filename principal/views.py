from django.shortcuts import render
from categoria.models import Categoria
from produto.models import Produto


def inicio(request):
    return render(request, "home.html")

def historia(request):
    return render(request, "historia.html")

def home(request):
    return render(request, "home.html")

def salgadas(request):
    try:
        salgadas = Categoria.objects.get(nome='Pizza Salgada')
        produtos = Produto.objects.filter(categoria=salgadas)
    except Categoria.DoesNotExist:
        produtos = []
    return render(request, "pzsalgada.html", {'produtos': produtos})

def doce(request):
    try:
        doce = Categoria.objects.get(nome='Pizza Doce')
        produtos = Produto.objects.filter(categoria=doce)
    except Categoria.DoesNotExist:
        produtos = []
    return render(request, "pzdoce.html", {'produtos': produtos})

def cadastrar_produto(request):
    categorias = Categoria.objects.all()

    if request.method == "POST":
        # Aqui você pode processar os dados do formulário se quiser salvar
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')
        categoria_id = request.POST.get('categoria')

        if nome and descricao and imagem and categoria_id:
            try:
                categoria = Categoria.objects.get(id=categoria_id)
                Produto.objects.create(
                    nome=nome,
                    descricao=descricao,
                    imagem=imagem,
                    categoria=categoria
                )
                return render(request, "cadastro_produto.html", {
                    "categorias": categorias,
                    "mensagem": "Produto cadastrado com sucesso!"
                })
            except Categoria.DoesNotExist:
                pass  # Você pode lidar com o erro aqui também

    return render(request, "cadastro_produto.html", {"categorias": categorias})
