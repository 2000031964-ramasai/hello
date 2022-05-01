from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
import urllib.request
import json
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# from .filters import OrderFilter

from .forms import *


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'contact'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],

            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'agriaquagrow@gmail', ['agriaquagrow@gmail'])
            except BadHeaderError:
                return redirect('index')
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def about(request):
    if request.method == "POST":
        return render(request, 'about.html')
    return render(request, 'about.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def services(request):
    return render(request, 'services.html')


@login_required(login_url='login')
def agritools(request):
    return render(request, 'agritools.html')


def logoutUser(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'title': 'Profile', 'form': form})


def home(request):
    return render(request, 'aflogin.html')


def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)
        api_url = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=ad6d91c541e7f84004e3201f55d89a05').read()
        api_url2 = json.loads(api_url)

        data = {
            "country": city,
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": api_url2['main']['temp'],
            "weather_pressure": api_url2['main']['pressure'],
            "weather_humidity": api_url2['main']['humidity'],
            "weather_icon": api_url2['weather'][0]['icon'],
        }

    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity": None,
            "weather_icon": None,
        }
    print(data['weather_icon'])
    return render(request, 'weather.html', {"city": city, "data": data})


class Statistics(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'statistics.html')



class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July'
        ]
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return Response(data)
