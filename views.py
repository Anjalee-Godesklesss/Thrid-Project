from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(" This is django first app")

def demo(request):
    return HttpResponse("Thanks For watching")
