from django.shortcuts import render, redirect
from .models import Nutricionista
from .forms import NutricionistaForm


def registrar(request):
    if request.method == "POST":
        form = NutricionistaForm(request.POST)
        if form.is_valid():
            nutri = form.save(commit=False)
            nutri.set_password(form.cleaned_data["senha"])
            nutri.save()
            return redirect("login")
    else:
        form = NutricionistaForm()

    return render(request, "registrar.html", {"form": form})


def login_view(request):
    erro = None

    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        try:
            nutri = Nutricionista.objects.get(email=email)

            if nutri.check_password(senha):
                return render(request, "bemvindo.html", {"nutri": nutri})
            else:
                erro = "Senha incorreta."
        except Nutricionista.DoesNotExist:
            erro = "Email não encontrado."

    return render(request, "login.html", {"erro": erro})
