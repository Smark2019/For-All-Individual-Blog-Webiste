from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "complaint"

urlpatterns = [

    path('addcomplaint/',views.addcomplaint,name = "add_complaint"),
    
    

]