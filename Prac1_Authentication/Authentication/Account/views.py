from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required





def Homeview(request):
    template_name='home.html'
    return render(request,template_name)

def Registeruserview(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='register.html'
    context={'form':form}
    return render(request,template_name,context)

def Loginuserview(request):
    if request.method == 'POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Cridential')
    template_name='login.html'
    return render(request,template_name)

@login_required
def Logoutview(request):
    logout(request)
    return redirect('login')

