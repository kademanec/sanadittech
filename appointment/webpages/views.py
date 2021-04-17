from django.http.request import HttpHeaders, HttpRequest
from django.shortcuts import render,redirect
from .models import BookApp
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"base.html")


def bookapp(request):
    if request.method == 'POST':
            if request.POST.get('username') and request.POST.get('first_name') and request.POST.get('date'):
                post=BookApp()
                post.username= request.POST.get('username')
                post.first_name= request.POST.get('first_name')
                post.save()
                
                return render(request, 'webpages/dashboard.html')  

    else:
            return render(request,'webpages/dashboard.html')


def viewapp(request):
    details=BookApp.objects.all()
    data={
        details:'details',
    }
    print(data['details'])
    pass