from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return JsonResponse({"error": "Um ou mais campos estão vazios."}, status=400)

    user = get_user_model()(username=username, email=email)
    user.set_password(password)
    user.save()

    return JsonResponse({"message": "Registro bem-sucedido."}, status=201)


def Login(request):
    return render(request, 'Login.html')


def Register(request):
    return render(request, 'Register.html')


def pagina_principal(request):
    return render(request, 'Home.html')
