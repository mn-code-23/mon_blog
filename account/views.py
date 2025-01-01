from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import LoginForm, Profil
from account.models import Utilisateur


# Create your views here.

# VUE login
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect")

    else:
        form = LoginForm()
    return render(request, "login.html", context={"form": form})

#VUE Singup
def singup_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Utilisateur.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, "singup.html", context={"form": form})
# VUE Logout
def logout_user(request):
    logout(request)
    return redirect('index')

#VUE profil
def Mon_profil(request, username):
    name = get_object_or_404(Utilisateur, username=username)
    user = request.user
    if request.method == 'POST':
        form = Profil(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Modification enregistrer avec succès")
            return redirect('Mon_profil', username=username)
        else:
            form.add_error(None, "Le bio doit avoir 500 caracteres maximum")
    else:
        form = Profil(instance=user)
    return render(request, "profil.html", context={"form": form,
                                                   "name": name})


