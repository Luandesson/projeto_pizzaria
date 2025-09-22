from django.shortcuts import render, redirect, get_object_or_404
from produto.models import Produto
from categoria.models import Categoria
from django.contrib import messages


# Create your views here.

def cadastrar(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')
        categoria_id = request.POST.get('categoria')

        if nome and descricao and imagem and categoria_id:
            categoria = Categoria.objects.get(id=categoria_id)
            produto = Produto(nome=nome, descricao=descricao, imagem=imagem, categoria=categoria)
            produto.save()
            return redirect('cadastro_produto.html')

    return render(request, 'cadastro_produto.html', {'categorias': categorias})


def buscarprod(request):
    produto = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        produto = Produto.objects.filter(nome__icontains=nome).first()
    return render(request, 'pesquisaproduto.html', {'produto': produto})


def excluirprod(request):
    if request.method == 'POST':
        codprod = request.POST.get('codprod')
        produto = get_object_or_404(Produto, id=codprod)
        produto.delete()

        messages.success(request, 'Produto excluído com sucesso!')

        return redirect('buscarprod')


def mostrarprod(request):
    if request.method == 'POST':
        codprod = request.POST.get('codprod')
        produto = get_object_or_404(Produto, id=codprod)
        categoria = Categoria.objects.all()
        return render(request, 'editarprod.html', {'produto': produto, 'categoria': categoria})
    messages.error(request, 'Acesso inválido. Use o formulário para editar um produto.')
    return redirect('buscarprod')  # redireciona para uma página existente

def atualizarprod(request):
    if request.method == 'POST':
        codprod = request.POST.get('codprod')
        produto = get_object_or_404(Produto, id=codprod)
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, id=categoria_id)

        produto.nome = nome
        produto.descricao = descricao
        produto.categoria =categoria
        if imagem:
            produto.imagem = imagem
        produto.save()

