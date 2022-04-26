from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def goodluck(request,pk):
    print(pk)
    return render(request,'navbar.html')