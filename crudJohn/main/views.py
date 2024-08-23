from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(response):
    return render(response,'index.html')