### USER REGISTER
<hr>

1. Yöntem, 

Django'nun default gelen user tablosu ile kayıt oluşturma, 
  
   *** bu durumda iki farklı secenek ile ilerlenebilir
      
     # a.  forms.py oluşturarak ilerleme #

forms.py  =>

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User # user ı kullan ve sadece username ve email aldık
        fields= ('username', 'email')



views.py =>


from .forms import UserForm

def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() :
           user = form.save()
          
       

           login(request, user)

           return redirect("home")

    context = {
     'form':form,
    }
    return render(request, "users/register.html", context) 


     # b.  views.py içinde user oluşturarak ilerleme #

*** bu yöntemde forms.py oluşturmadık!!!!

from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() :
           user = form.save()
          
       

           login(request, user)

           return redirect("home")

    context = {
     'form':form,
    }
    return render(request, "users/register.html", context) 


**** YUKARIDAKİ HER İKİ YÖNTEM DE REGISTER.HTML SAYFASINA YÖNLENDİRDİK ****

###   USER LOGOUT 

from django.contrib.auth import  logout


def user_logout(request):

   messages.success(request, 'You logged out') 
   logout(request)
   return redirect("home")


LOGOUT İSLEMİNDE TEMPLATE SAYFA OLUŞTURMAYA GEREK YOK  



###RELA



