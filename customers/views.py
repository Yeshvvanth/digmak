from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,CustomerForm
from . models import CustomerProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('customer:home')
        else:
            messages.info(request,"Incorrect UserName and Password")

    return render(request,'customer/login.html')

def logoutUser(request):
    logout(request)
    return redirect('customer:login')


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'User has been created successfully'+ user)
            return redirect('customer:login')
    context = {'form':form}
    return render(request,'customer/register.html',context)


@login_required(login_url='customer:login')
def home(request):
    return render(request,'customer/customer_home.html')

def customer_profile(request):
    customer= request.user.customerprofile
    form = CustomerForm(instance=customer)

    if request.method=="POST":
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request,'customer/profile.html',context)