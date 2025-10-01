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
        # ID CONFIRMADO ANTERIORMENTE: 6 (Pizzas salgadas)
        ID_PIZZAS_SALGADAS = 6
        categoria_salgada = Categoria.objects.get(pk=ID_PIZZAS_SALGADAS)

        # Filtra todos os produtos que apontam para essa categoria ID
        produtos = Produto.objects.filter(categoria=categoria_salgada)
    except Categoria.DoesNotExist:
        # Se a categoria não for encontrada (ID errado), retorna lista vazia.
        produtos = []

    return render(request, "salgadas.html", {'produtos': produtos})


def doce(request):
    try:
        # ID CORRIGIDO: 5 (Pizzas doce)
        ID_PIZZAS_DOCES = 5
        categoria_doce = Categoria.objects.get(pk=ID_PIZZAS_DOCES)

        produtos = Produto.objects.filter(categoria=categoria_doce)
    except Categoria.DoesNotExist:
        produtos = []

    return render(request, "doce.html", {'produtos': produtos})


def cadastrar_produto(request):
    categorias = Categoria.objects.all()

    if request.method == "POST":
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
                pass

    return render(request, "cadastro_produto.html", {"categorias": categorias})
