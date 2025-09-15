from django.shortcuts import render

# Create your views here.
def cadastrar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        if nome:
            categoria = Categoria(nome=nome)
            categoria.save()
            return redirect('cadcategoria.html')

    return render(request, 'cadcategoria.html')