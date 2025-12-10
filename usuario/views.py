from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
            #livros = Livro.objects.all()
            #return render(request, 'livros.html', {'livros': livros})
            return redirect('inicio')
        else:
            return HttpResponse('Usuario ou senha invalidos')

def logout_usuario(request):
    logout (request)
    return render(request, 'index.html')

@login_required
def edita_usuario(request):
    usuario = request.user
    
    if request.method == "POST":
        usuario.username = request.POST.get("username")
        usuario.email = request.POST.get("email")

        # Se quiser permitir troca de senha:
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if senha:
            if senha != confirmar_senha:
                return render(request, "editar_usuario.html", {
                    "erro": "As senhas não coincidem!",
                    "usuario": usuario
                })
            usuario.set_password(senha)

        usuario.save()
        return redirect("inicio")  # redirecionar para onde quiser

    return render(request, "perfil.html", {"usuario": usuario})

    # if request.method == "POST":
    #     livro.titulo = request.POST['titulo']
    #     livro.autor = request.POST['autor']
    #     livro.ano_publicacao = request.POST['ano_publicacao']
    #     livro.editora = request.POST['editora']
    #     livro.save()
    #     return redirect('cadastro_livro')

    # return render(request, 'livros.html', {'livros': livros, 'livro_editar': livro}) 