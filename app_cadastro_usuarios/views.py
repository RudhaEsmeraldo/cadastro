from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # salvar dados da tela para o DB
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade') 
    novo_usuario.save()
    # Exibir todos os usuários novos em uma tela
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    # Retornar dados para pag de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)