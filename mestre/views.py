from django.shortcuts import render, get_object_or_404
from .models import Aula, Progresso
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from trilhas.models import Avaliacao


def aularender(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)

    # 👉 marca progresso automaticamente
    if request.user.is_authenticated:
        Progresso.objects.get_or_create(
            usuario=request.user,
            aula=aula
        )

    aula_anterior = Aula.objects.filter(
        trilha=aula.trilha,
        id__lt=aula.id
    ).order_by('-id').first()

    proxima_aula = Aula.objects.filter(
        trilha=aula.trilha,
        id__gt=aula.id
    ).order_by('id').first()

    return render(request, "mestre/aularender.html", {
        "aula": aula,
        "aula_anterior": aula_anterior,
        "proxima_aula": proxima_aula
    })

@login_required
def cadastrar_aula(request):
    if request.method == "POST":
        trilha = request.POST.get("trilha")
        titulo = request.POST.get("titulo")
        conteudo = request.POST.get("conteudo")
        imagem = request.POST.get("imagem")

        Aula.objects.create(
            trilha=trilha,
            titulo=titulo,
            conteudo=conteudo,
            imagem=imagem
        )

        return redirect("cadastrar_aula")

    return render(request, "mestre/cadastrar_aula.html")

def avaliacao_final(request, aula_id):
    if request.method == "POST":
        nota = request.POST.get("avaliacao")

        # marca a trilha como concluída (pela última aula)
        Avaliacao.objects.get_or_create(
            usuario=request.user,
            aula=f"final_{aula_id}",  # simples e funcional
            defaults={"avaliacao": nota}
        )

        return redirect("edita_usuario")  # perfil/progresso

    aula = get_object_or_404(Aula, id=aula_id)

    return render(request, "mestre/avaliacao_final.html", {
        "aula": aula
    })