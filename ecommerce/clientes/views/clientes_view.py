from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login

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
    return render(request, 'login.html')

def logout_user(request):
    return redirect(reverse('produtos:listar_produtos'))