from django.shortcuts import render
from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_protect
from .models import destination

# Create your views here.

def home(request):
    dests=destination.objects.all()
    return render(request,'index.html',{'dest1':dests,'name':'Avinash'})
@csrf_protect
def add(request):
    sum=0
    if(request.POST['num1']!="" and request.POST['num1']!=""):
        val1= request.POST['num1']
        val2=request.POST['num2']
        sum = int(val1)+int(val2)
        return render(request,'result.html',{'Sum':sum})
    else:
        return render(request,'index.html',{"nam2":" Yes, Enter Values"})
def display(request):
    return render(request,'Display.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')

