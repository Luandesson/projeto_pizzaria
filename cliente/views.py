from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from cliente.models import Cliente
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def cadastrar_cli(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST['email']
        endereco = request.POST['endereco']

        # Certifique-se de que a URL de redirecionamento está correta
        # Por exemplo, para a página de login:
        # return redirect('login')
        # ou para a página inicial:
        # return redirect('/')

        usuario = User.objects.create_user(username=usuario, password=senha, email=email)

        Cliente.objects.create(usuario=usuario,
                               nome=nome,
                               email=email,
                               endereco=endereco
                               )
        return redirect('home')
    return render(request, 'cadcli.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('menu_cli')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return render(request, 'login.html')

    return render(request, 'login.html')

def menu_cli(request):
    return render(request, 'menucli.html')
