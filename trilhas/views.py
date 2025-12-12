from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Avaliacao

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def teste1(request):
    return render(request, "teste1.html")

def teste2(request):
    return render(request, "teste2.html")

def testefinal(request):
    return render(request, "testefinal.html")

def saibamais(request):
    return render(request, "saibamais.html")

def avaliar_trilha(request):
    if request.method == "POST":
        nota = request.POST.get("nota")

        if nota:
            messages.success(request, f"Sua avaliação foi registrada com {nota} estrelas!")
        else:
            messages.error(request, "Por favor, selecione uma nota antes de enviar.")

        return redirect('testefinal')  # vá para onde quiser

    return redirect('testefinal')

def concluir_aula(request, aula_id):
    if request.method == "POST":
        nota = request.POST.get("avaliacao")

        registro, _ = Avaliacao.objects.get_or_create(
            usuario=request.user,
            aula=aula_id
        )

        if nota:
            registro.avaliacao = int(nota)
            registro.save()

        return redirect("perfil")
    return redirect("inicio")
