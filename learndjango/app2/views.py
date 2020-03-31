from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.http import HttpResponse
# Create your views here.


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email_id=request.POST['email_id']
        password=request.POST['password']
        x=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email_id,password=password)
        x.save()
        print("user created")
        return redirect('/')

    else:
        return render(request, 'b.html')