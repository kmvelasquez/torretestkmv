from django.shortcuts import render
from .forms import CreateUserForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.

def Index(request):
    return render(request,'index.html')

def RegisterPage(request):
    if request.user.is_authenticated:
        print("Redirection")
        #return redirect ('/profile')
    
    else:
        form= CreateUserForm()
        if request.method == "POST":
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                #return redirect('login')

        context={'form':form}
        return render(request,'register.html', context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('/profile')
        
    else:
        if request.method == "POST":
            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or password are incorrect!')
    context={}
    return render(request,'login.html', context)
