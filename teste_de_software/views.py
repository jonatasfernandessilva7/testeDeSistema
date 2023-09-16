from django.shortcuts import render, HttpResponse, redirect
from .forms import CadastroForm, LoginForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages


# Create your views here.

def cadastro(request):
    form = CadastroForm()
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            name = form['name'].value()
            surname = form['surname'].value()
            username = form['username'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('cadastro')
            
            if User.objects.filter(username=username) != str:
                messages.error(request, 'nome inválido')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                first_name = name,
                last_name = surname,
                username=username,
                email=email,
                password=password
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')
    return render(request, "usuarios/cadastro.html", {'form': form})

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

        usuario = auth.authenticate(
            request,
            username=username,
            password=password
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{username} logado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})
