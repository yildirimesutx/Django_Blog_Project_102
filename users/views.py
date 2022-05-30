
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
# from .forms import UserForm
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def test(request):
    return render(request, 'users/test.html')

def user_logout(request):

   messages.success(request, 'You logged out') 
   logout(request)
   return redirect("home")









def register(request):
    form =  UserCreationForm()
   

    context = {
        'form':form
    }
    return render(request, "users/register.html", context) 