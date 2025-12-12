from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from trilhas.models import Avaliacao
TOTAL_AULAS = 3

# Create your views here.

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def cadastro_usuario(request):
    if request.method == "GET":
        return render(request, "cadastro.html")

    elif request.method == "POST":
        nome_usuario = request.POST.get("nome_usuario", "").strip()
        email = request.POST.get("email", "").strip()
        senha = request.POST.get("senha", "").strip()

        # Verificação de campos vazios
        if not all([nome_usuario, email, senha]):
            return HttpResponse("Por favor, preencha todos os campos obrigatórios.")

        # Verifica se usuário já existe
        if User.objects.filter(username=nome_usuario).exists():
            return HttpResponse("Usuário já cadastrado!")

        # Cria o usuário
        usuario = User.objects.create_user(
            username=nome_usuario,
            email=email,
            password=senha,
        )
        usuario.save()

        return redirect("inicio")
 
def login_usuario(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']

        usuario = authenticate(username=nome_usuario, password=senha)
        if usuario:
            login(request, usuario)
            # Verifique se o usuário é admin
            if usuario.is_superuser:
                return redirect('cadastrar_aula')  # ou o nome da URL que você deseja
            else:
                return redirect('inicio')
        else:
            return HttpResponse('Usuário ou senha inválidos')

def logout_usuario(request):
    logout (request)
    return render(request, 'index.html')

def edita_usuario(request):
    usuario = request.user

    if request.method == "POST":
        usuario.username = request.POST.get("username")
        usuario.email = request.POST.get("email")

        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if senha:
            if senha != confirmar_senha:
                return render(request, "perfil.html", {
                    "erro": "As senhas não coincidem!",
                    "usuario": usuario
                })
            usuario.set_password(senha)

        usuario.save()
        return redirect("edita_usuario")

    # 👉 CÁLCULO DE PROGRESSO
    concluidas = Avaliacao.objects.filter(usuario=usuario).count()
    progresso = int((concluidas / TOTAL_AULAS) * 100)

    return render(request, "perfil.html", {
        "usuario": usuario,
        "concluidas": concluidas,
        "total": TOTAL_AULAS,
        "progresso": progresso
    })