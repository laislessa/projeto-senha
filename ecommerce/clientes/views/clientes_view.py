from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib import messages

from clientes.models.endereco import Endereco
from ..forms import EnderecoForm
from ..models.endereco import Endereco


def criar_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = get_user_model()
        usuario = user (
            email=email,
            password=password
        )
        usuario.set_password(password)
        usuario.save()
        ##print(f'{email} - {password}')
    return render(request, 'criar_cliente.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            username=email,
            password=password
        )
        if user:
            login(request,user)
            messages.success(request,'Usuário Logado')
            return redirect('produtos:listar_produtos')
            #print('Usuario Autenticado')
        else:
            print('Usuario não existe')
        print('f{email} - {password}')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect(reverse('produtos:listar_produtos'))

def cadastrar_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            rua = form.cleaned_data['rua']
            numero = form.cleaned_data['numero']
            Endereco.objects.create(
                rua=rua,
                numero=numero,
                user=request.user
            )
    else:
         form = EnderecoForm()
    return render(request, 'criar_enderecos.html',{'form':form})
