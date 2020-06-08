from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *
# Create your views here.
def home(request):
    return render(request,'index.html')


def cooking(request):
    cook1 = cooking1.objects.all()
    return render(request,'cooking.html', {'cook1': cook1})
def electronics(request):
    ele1 = electronics1.objects.all()
    return render(request, 'electronics.html', {'ele1':ele1})
def essentials(request):
    esse1 = essentials1.objects.all()
    return render(request, 'essentials.html', {'esse1':esse1})
def furniture(request):
    furn1 = furniture1.objects.all()
    return render(request, 'furniture.html', {'furn1':furn1})
def vehicle(request):
    veh1 = vehicles1.objects.all()
    return render(request, 'vehicle.html',{'veh1':veh1})
def housing(request):
    hous1 = housing1.objects.all()
    return render(request, 'housing.html',{'hous1':hous1}) 

