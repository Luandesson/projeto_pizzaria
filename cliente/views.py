# cliente/views.py (Código Completo Corrigido)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from cliente.models import Cliente
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages


def cadastrar_cli(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST['email']
        endereco = request.POST['endereco']
        usuario = User.objects.create_user(username=usuario, password=senha, email=email)

        Cliente.objects.create(usuario=usuario,
                               nome=nome,
                               telefone=telefone,
                               email=email,
                               endereco=endereco
                               )
        messages.success(request, 'Cliente cadastrado com sucesso')
        return redirect('home')
    return render(request, 'cadcli.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Garante que o username está na sessão (útil para o template menucli.html)
            request.session['username'] = username

            return redirect('menu_cli')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return render(request, 'login.html')

    return render(request, 'login.html')


def menu_cli(request):
    return render(request, 'menucli.html')


def logout_view(request):
    request.session.pop('username', None)
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso.')
    return redirect('login')