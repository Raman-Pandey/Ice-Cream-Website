from django.contrib import admin
from django.urls import path
from dev import views

urlpatterns = [
    path("",views.index,name='dev'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact')
]