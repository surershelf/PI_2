from django.shortcuts import render


def Login(request):
    return render(request, 'Login.html')


def Register(request):
    return render(request, 'Register.html')


def pagina_principal(request):
    return render(request, 'Home.html')