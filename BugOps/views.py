# from curses.ascii import HT
from xmlrpc.client import DateTime
from django.http import HttpResponse
from django.shortcuts import render

import datetime as d

# from . import

def home(request):
    return render(request, 'base.html')
    # return HttpResponse("<h1>Arrived on the home page for BugOps!<h1>")

def index(request):
    return HttpResponse("<h1>You have arrived on the index for the BugOps proj.<h1>")

def login(request):
    return render(request, 'registration/login.html')

def login_request(request):
    if request.method == "POST":
        

def datetime(request):
    dt = d.datetime.today()
    return HttpResponse(f"The current datetime is {dt}")
