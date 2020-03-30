from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,'home.html',{'titles':'gajab cha baa..'})

def profile(request):
    return HttpResponse("Profile Page")

def expression(request):
    a=int(request.POST['txt1'])
    b=int(request.POST['txt2'])
    c=a+b
    return render(request, 'home.html', {'titles':'Form Value','result': c})