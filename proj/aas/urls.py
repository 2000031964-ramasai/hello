
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('agritools/', views.agritools, name='agritools'),
    path('profile/', views.profile, name='profile'),

]
