from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render




# Create your views here.
def index(request):
    return render(request,'index.html')

def login_student(request):
    return render(request,'student/login_student.html')

def login_teach(request):
    return render(request,'teach/login_teach.html')

def choice(request):
    return render(request,'choice.html')
    
def dashboard_s(request):
    return render(request,'student/dashboard_s.html')
    
def dashboard_t(request):
    return render(request,'teach/dashboard_t.html')