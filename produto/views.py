from django.shortcuts import render, redirect, get_object_or_404
from produto.models import Produto
from categoria.models import Categoria
# Create your views here.

def cadastrar(request):
    categorias = Categoria.objects.all()
    if request.method =='POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')
        categoria_id = request.POST.get('categoria')

        if nome and descricao and imagem and categoria_id:
            categoria = Categoria.objects.get(id=categoria_id)
            produto = Produto(nome=nome, descricao=descricao, imagem=imagem, categoria=categoria)
            produto.save()
            return redirect('cadastro_produto.html')

    return render(request, 'cadastro_produto.html', {'categorias':categorias})
def buscarprod(request):
    produto = None
    if request.method=='POST':
        nome = request.POST.get('nome')
        produto = Produto.objects.filter(nome__icontains=nome).first()
    return render(request, 'pesquisaproduto.html', {'produto':produto})

def excluirprod(request):
    if request.method == 'POST':
        codprod = request.POST.get('codprod')
        produto = get_object_or_404(Produto, id=codprod)
        produto.delete()

        return redirect('buscarprod')