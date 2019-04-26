# Create your views here.
from django.http import HttpResponse
import datetime
from django.shortcuts import render

spacecrafts = {"MAVEN":{"full_name":"Mars Atmosphere and Volatile Evolution", "agency":"NASA", "launch_date":"November 2013", "mission_objective":"Study of Martian atmosphere"},
               "MRO":{"full_name":"Mars Reconnaissance Orbiter", "agency":"NASA", "launch_date":"August 2005", "mission_objective":"Imaging of Martian surface"},
               }

spacecraft = {"name":"MAVEN", "agency":"NASA", "launch_date":"November 2013", "mission_objective":"Study of Martian atmosphere"}

def home(request):
    return render(request, 'about/home.html')

def about(request):
    return render(request, 'about/home.html')

def maven(request):
    return render(request, 'about/spacecraft_template.html', context=spacecrafts["MAVEN"])

def mro(request):
    return render(request, 'about/spacecraft_template.html', context=spacecrafts["MRO"])
