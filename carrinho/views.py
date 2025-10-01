from django.shortcuts import render, redirect, get_object_or_404
from produto.models import Produto

def addcarrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        carrinho[str(produto_id)] = 1

    request.session['carrinho'] = carrinho
    return redirect('home')

def mostrarcarrinho(request):
    carrinho = request.session.get('carrinho', {})
    carrinho_itens = []
    total = 0
    for produto_id, quantidade in carrinho.items():
        produto = get_object_or_404(Produto, id=produto_id)
        item_total = produto.valor * quantidade
        total += item_total

        carrinho_itens.append({
            'produto': produto,
            'quantidade': quantidade,
            'item_total': item_total,
        })
    return render(request, 'carrinho.html', {'carrinho_itens': carrinho_itens, 'total': total})