from django.shortcuts import render,redirect
from .forms import Registerform,Loginform
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here..


def registerUser(request):
    if request.method == "POST":
        form = Registerform(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)
            messages.success(request,username+" Başarıyla Kayıt Oldunuz !")
            return redirect("index")
        else:
            context = {"form":form}
            messages.warning(request," Hatalı Form Doldurma İşlemi Yaptınız !")
            return render(request,"register.html",context)
    else:
        form = Registerform()
        context = {"form":form}
        return render(request,"register.html",context)
    
def loginUser(request):
    form = Loginform(request.POST or None)
    context = { "form" : form}
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password  = form.cleaned_data.get("password")

            user     = authenticate(username = username,password = password) 
            if user is None:
                messages.warning(request,"Kullanıcı Adı ya da Parola HATALI !")

                return render (request,"login.html",context)

            messages.success(request,username+" Başarıyla Giriş Yaptınız")
            login(request,user)
            return redirect("index")
        
        else:
            messages.warning(request," HATALI Giriş Yaptınız")
            return render (request,"login.html",context)
    else:
        form = Loginform()
        context = {"form":form}
        return render(request,"login.html",context)


    
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")


