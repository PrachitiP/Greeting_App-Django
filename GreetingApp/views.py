import greet as greet
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
# from .forms import MessageForm
from .models import GreetingCard

def insert(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        user = GreetingCard(name=name, message=message)

        user.save()
        return redirect('/display')
    return render(request,'index.html')

def display(request):
    context = {
        "users": GreetingCard.objects.all()
    }
    return render(request, 'display.html',context)

def update(request, id):
    userid=id
    if request.method=='POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        user_object = GreetingCard(name=name, message=message, id=userid)
        user_object.save()
        return redirect('/display')
    else:
        context = {
            "users" : GreetingCard.objects.filter(id=userid)
        }
        return render(request,'update.html',context)

def delete(request, id):
    userid=id
    user = GreetingCard.objects.get(id=userid)
    user.delete()
    return redirect('/display')
