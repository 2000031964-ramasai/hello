from django.http import HttpResponse
from django.shortcuts import render, redirect
from translate import Translator
from MySQLdb import*
from .forms import *


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        return HttpResponse(translation)
    return render(request, 'about.html')


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'login.html', {'form': form})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'register.html', {'form': form})


def services(request):
    return render(request, 'services.html')
