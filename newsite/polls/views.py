from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")
# Create your views here.
# to call the view, map this to a URL with URLconf
# create URLconf in the polls dir and create file urls.py
