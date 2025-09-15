from django.shortcuts import render, redirect
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
        
        if nome and descricao and imagem:
            produto = Produto(nome=nome, descricao=descricao, imagem=imagem)
            produto.save()
            return redirect('cadastro_produto.html')

    return render(request, 'cadastro_produto.html')