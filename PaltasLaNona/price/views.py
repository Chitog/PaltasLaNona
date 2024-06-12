from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('pricing')
            except:
                return HttpResponse('Usuario ya existente')
        else:
            return HttpResponse('Contraseñas no coinciden')
            
    
def create_pricing(request):
    
    if request.method == 'GET':
        return render(request, 'create_pricing.html', {
            'form': CreatePricing
        })
    else:
        try:
            form = CreatePricing(request.POST)
            new_pricing = form.save(commit=False)
            new_pricing.save()
            return redirect('/')
        except ValueError:
            return render(request, 'create_pricing.html',{
                'form': CreatePricing,
                'error': 'Please provide valid data'
            })
            
def pricing(request):
    
    sol_cotizacion = solicitud_cotizacion.objects.all()
    
    return render(request, 'pricing.html', {'sol_cotizacion': sol_cotizacion})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('pricing')