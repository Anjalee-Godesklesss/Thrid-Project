from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return  render(request, "base.html",{"name":"Arjuna"})

def demo(request):
    return render (request, "demo.html",{"age":"30"})