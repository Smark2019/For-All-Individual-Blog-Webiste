from django.shortcuts import render,redirect,HttpResponse
from .forms import Complaintform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addcomplaint(request):
    form = Complaintform(request.POST or None)
    content = {"form":form}
    if request.method == "POST":
        if form.is_valid():
            article = form.save(commit=False)
            article.author =request.user
            article.save()

            messages.success(request,"Başarılı Şekilde Şikayetiniz & Öneriniz Kaydedildi")
            return redirect("index")
    return render (request,"complaint.html",content)
    