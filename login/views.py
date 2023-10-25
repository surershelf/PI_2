from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Usuario

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crie uma instância do modelo e salve os dados no banco de dados
            novo_usuario = Usuario(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                senha=form.cleaned_data['senha'],
                data_nascimento=form.cleaned_data['data_nascimento'],
                genero=form.cleaned_data['genero']
            )
            novo_usuario.save()
            return redirect('sucesso')  # Redirecione para uma página de sucesso
        else:
            # O formulário não é válido, retorne a página com erros
            return render(request, 'seu_template.html', {'form': form})

    else:
        form = RegistroForm()

    return render(request, 'seu_template.html', {'form': form})


def Login(request):
    return render(request, 'Login.html')


def Register(request):
    return render(request, 'Register.html')


def pagina_principal(request):
    return render(request, 'Home.html')
